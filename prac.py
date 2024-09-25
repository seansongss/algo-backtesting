import yfinance as yf
import requests

session = requests.Session()
session.verify = False
data = yf.download('MSFT', start='2020-10-25', end='2020-12-31', session=session)
tick_data = yf.Ticker('MSFT', session=session)
print(data)
df = tick_data.get_balance_sheet()
print(tick_data.news[0])
# print(df)