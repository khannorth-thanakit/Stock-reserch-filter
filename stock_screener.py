import yfinance as yf
import time
import pandas  as  pd
from google.colab import data_table

def get_stock_data(stock_symbol, sleep_time=1):
    """
    ดึงข้อมูลหุ้นจาก yfinance และหน่วงเวลาหลังการดึงข้อมูลแต่ละครั้ง
    Args:
        stock_symbol (str): ชื่อย่อหุ้น
        sleep_time (int): เวลาหน่วง (วินาที)
    Returns:
        dict: ข้อมูลหุ้น
    """
    try:
        # หน่วงเวลาระหว่างการดึงข้อมูล
        time.sleep(sleep_time)

        stock = yf.Ticker(stock_symbol)
        info = stock.info

        # ดึงข้อมูลที่จำเป็น
        market_price = info.get("currentPrice")
        book_value = info.get("bookValue")
        PE_ratio = info.get("trailingPE")
        EPS = info.get("trailingEps")
        tot_Revenue = info.get("totalRevenue")
        net_income = info.get("netIncomeToCommon")
        total_debt = info.get("totalDebt")

        # ดึงงบการเงินย้อนหลัง
        financials = stock.financials  # รายได้และค่าใช้จ่าย
        net_income = financials.loc["Net Income", :]  # กำไรสุทธิหลังหักภาษี (Net Income)
        net_income_sum = net_income[:3].sum()  # กำไรสุทธิรวม 3 ปีย้อนหลัง

        return {
            "Stock Symbol": stock_symbol,
            "Market Price": market_price,
            "Book Value": book_value,
            "PE Ratio": PE_ratio,
            "EPS": EPS,
            "Total Revenue": tot_Revenue,
            "Net Income": net_income,
            "Total Debt": total_debt,
            "Net Income (3 years total)": net_income_sum,
        }
    except Exception as e:
        print(f"Error fetching data for {stock_symbol}: {e}")
        return None

def filter_stocks(stock_symbols, sleep_time=1):
    """
    กรองหุ้นตามเงื่อนไข
    Args:
        stock_symbols (list): รายชื่อหุ้น
        sleep_time (int): เวลาหน่วง (วินาที)
    Returns:
        list: รายชื่อหุ้นที่ผ่านเงื่อนไข
    """
    filtered_stocks = []

    for symbol in stock_symbols:
        stock_data = get_stock_data(symbol, sleep_time=sleep_time)

        if stock_data:
            market_price = stock_data["Market Price"]
            book_value = stock_data["Book Value"]
            eps = stock_data["EPS"]
            total_debt = stock_data["Total Debt"]
            net_income_sum = stock_data["Net Income (3 years total)"]


            # ตรวจสอบเงื่อนไข ราคาหุ้น < มูลค่าหุ้นทางบัญชี 30% (ก็คือ 70%) และกำไรเป็น +
            if market_price and book_value and market_price < (book_value * 0.7) and eps is not None and eps  > 0 and net_income_sum is not None and total_debt is not None and net_income_sum > total_debt:
                #book value * (1-0.3) = ราคาหลังลดแล้ว //ราคาหลังลดราคา = ราคาเต็ม * (1-อัตราส่วนลด)
                filtered_stocks.append(stock_data)

    return filtered_stocks

def save_to_excel(data, filename):
    try:
        # แปลงข้อมูลเป็น DataFrame
        df = pd.DataFrame(data)

        # บันทึกลงไฟล์ Excel
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to Excel: {e}")

# กรองหุ้นที่ผ่านเงื่อนไข
result = filter_stocks(stock_symbols, sleep_time=2)

save_to_excel(result, "filtered_stocks.xlsx")


# แสดงผลลัพธ์
if result:
    print("Stocks where Market Price < 70% of Book Value and eps > 0 and net_income_sum > total_debt :")
    for stock in result:
        print(stock)
else:
    print("No stocks meet the criteria.")
