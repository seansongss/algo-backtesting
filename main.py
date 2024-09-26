from utils.data_fetcher import fetch_data
from utils.backtesting import backtest_strategy
from utils.get_signals import get_signals
from utils.plot_graph import plot_graph

from config import INITIAL_CAPITAL

def main():
    # Fetch data
    data = fetch_data()

    # Apply strategy
    signals = get_signals(data)

    # Backtest strategy
    portfolio = backtest_strategy(data, signals, INITIAL_CAPITAL)

    # Example of calculating portfolio total value
    final_portfolio_value = portfolio['Total'].iloc[-1]
    
    # Example calculation of total return
    total_return = (final_portfolio_value - INITIAL_CAPITAL) / INITIAL_CAPITAL * 100
    
    # Print the total return
    print(f'Initial Capital: ${INITIAL_CAPITAL}')
    print(f'Initial Capital: ${final_portfolio_value:.1f}')
    print(f'Total Return: {total_return:.2f}%')

    # Plot results
    plot_graph(data, signals)

if __name__ == "__main__":
    main()
