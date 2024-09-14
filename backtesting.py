import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the ticker symbol
ticker = 'AAPL'  # Example: Apple Inc.

# Define the date range
start_date = '2020-01-01'
end_date = '2023-01-01'

# Fetch the data
data = yf.download(ticker, start=start_date, end=end_date)

# Display the first few rows
print(data.head())
