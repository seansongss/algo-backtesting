import pandas as pd

from config import COMMISSION, TICKER

pd.set_option('future.no_silent_downcasting', True)

def backtest_strategy(data, signals, initial_capital):
    # Initialize portfolio DataFrame
    portfolio = pd.DataFrame(index=signals.index, columns=[TICKER, "Holdings", "Cash", "Commission", "Total", "Returns"]).fillna(0.0)
    portfolio[TICKER] = data['Adj Close']
    
    # Initial values for cash and holdings
    cash = initial_capital
    holdings = 0
    commission_total = 0
    
    # Iterate through signals
    for date, row in signals.iterrows():
        price = portfolio.at[date, TICKER]
        signal = row['Signal']
        position = row['Positions']
        
        if signal == 1 and position == 0:  # Buy signal
            # Calculate how much stock can be bought with available cash (minus commission)
            if cash > COMMISSION:  # Ensure commission can be deducted from cash
                # Calculate the number of shares to buy
                shares_to_buy = (cash - COMMISSION) // price
                if shares_to_buy > 0:
                    # Update holdings, cash, and commission
                    holdings += shares_to_buy
                    cash -= shares_to_buy * price + COMMISSION
                    commission_total += COMMISSION
                    portfolio.at[date, "Holdings"] = holdings
                    portfolio.at[date, "Commission"] = COMMISSION
        
        elif signal == 1 and position == 1 and holdings > 0:  # Sell signal
            # Sell all holdings
            cash += holdings * price - COMMISSION
            commission_total += COMMISSION
            portfolio.at[date, "Holdings"] = 0  # After selling, no holdings
            holdings = 0
            portfolio.at[date, "Commission"] = COMMISSION
        
        # Update portfolio with cash, total value, and returns
        portfolio.at[date, "Cash"] = cash
        portfolio.at[date, "Total"] = cash + (holdings * price)  # Total is cash + value of holdings
        if date != signals.index[0]:  # Skip the first row
            portfolio.at[date, "Returns"] = portfolio.at[date, "Total"] - portfolio.at[signals.index[0], "Total"]
    
    print(portfolio)
    return portfolio
