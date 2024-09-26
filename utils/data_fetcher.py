import requests
import yfinance as yf

from config import START_DATE, END_DATE, TICKER, IS_AIRGAPPED

def fetch_data(ticker=TICKER, start_date=START_DATE, end_date=END_DATE):
    session = None
    # configure session if it airgapped network
    if IS_AIRGAPPED:
        session = requests.Session()
        session.verify = False

    data = yf.download(ticker, start=start_date, end=end_date, session=session)
    return data
