import pandas as pd
import numpy as np
from config import COMMISSION, TICKER

def backtest_strategy(data, signals, initial_capital=100000.0):
    positions = pd.DataFrame(index=signals.index).fillna(0.0)
    positions[TICKER] = 100 * signals['Signal']  # Example: 100 shares

    portfolio = positions.multiply(data['Adj Close'], axis=0)
    portfolio['Holdings'] = positions.multiply(data['Adj Close'], axis=0).sum(axis=1)
    portfolio['Cash'] = initial_capital - (positions.diff().multiply(data['Adj Close'], axis=0)).sum(axis=1).cumsum()
    
    # Deduct commission
    trade_costs = (positions.diff().abs() * COMMISSION).sum(axis=1)
    portfolio['Cash'] -= trade_costs.cumsum()
    
    portfolio['Total'] = portfolio['Holdings'] + portfolio['Cash']
    portfolio['Returns'] = portfolio['Total'].pct_change()

    return portfolio
