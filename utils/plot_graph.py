import matplotlib.pyplot as plt
from config import STRATEGY, SHORT_WINDOW, LONG_WINDOW

def plot_graph(data, signals):
    plt.figure(figsize=(14,7))

    match STRATEGY:
        case 'moving_average':
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
        
        case 'mean_reversion':
            plt.plot(data['Close'], label='Close Price', alpha=0.5)
            plt.plot(signals.loc[signals['Positions'] == 1.0].index,
                    data['Close'][signals['Positions'] == 1.0],
                    '^', markersize=10, color='g', label='Buy Signal')
            plt.plot(signals.loc[signals['Positions'] == -1.0].index,
                    data['Close'][signals['Positions'] == -1.0],
                    'v', markersize=10, color='r', label='Sell Signal')
    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()