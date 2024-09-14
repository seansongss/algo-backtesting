import matplotlib.pyplot as plt
from utils.data_fetcher import fetch_data
from utils.backtesting import backtest_strategy
from strategies.moving_average import moving_average_strategy
from config import SHORT_WINDOW, LONG_WINDOW

def main():
    # Fetch data
    data = fetch_data()

    # Apply strategy
    signals = moving_average_strategy(data)

    # Backtest strategy
    portfolio = backtest_strategy(data, signals)
    
    print(portfolio)

    # Plot results
    plt.figure(figsize=(14,7))
    plt.plot(data['Close'], label='Close Price', alpha=0.5)
    plt.plot(data['SMA_Short'], label=f'{SHORT_WINDOW}-day SMA', alpha=0.5)
    plt.plot(data['SMA_Long'], label=f'{LONG_WINDOW}-day SMA', alpha=0.5)
    plt.plot(signals.loc[signals['Positions'] == 1.0].index,
             data['Close'][signals['Positions'] == 1.0],
             '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(signals.loc[signals['Positions'] == -1.0].index,
             data['Close'][signals['Positions'] == -1.0],
             'v', markersize=10, color='r', label='Sell Signal')
    plt.title('Moving Average Crossover Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
