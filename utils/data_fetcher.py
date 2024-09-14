import yfinance as yf
from config import START_DATE, END_DATE, TICKER

def fetch_data(ticker=TICKER, start_date=START_DATE, end_date=END_DATE):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data
