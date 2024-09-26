from utils.data_fetcher import fetch_data
from utils.backtesting import backtest_strategy
from utils.get_signals import get_signals
from utils.plot_graph import plot_graph

def main():
    # Fetch data
    data = fetch_data()

    # Apply strategy
    signals = get_signals(data)

    # Backtest strategy
    portfolio = backtest_strategy(data, signals)
    
    # Example of calculating portfolio total value
    final_portfolio_value = portfolio['Total'].iloc[-1]
    
    # Example calculation of total return
    initial_capital = 100000.0  # Example initial capital
    total_return = (final_portfolio_value - initial_capital) / initial_capital * 100
    
    # Print the total return
    print(f'Total Return: {total_return:.2f}%')

    # Plot results
    plot_graph(data, signals)

if __name__ == "__main__":
    main()
