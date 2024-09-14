import pandas as pd
import numpy as np
from config import SHORT_WINDOW

def mean_reversion_strategy(data):
    # Calculate mean and standard deviation
    rolling_mean = data['Close'].rolling(window=SHORT_WINDOW).mean()
    rolling_std = data['Close'].rolling(window=SHORT_WINDOW).std()

    # Generate signals
    signals = pd.DataFrame(index=data.index)
    signals['Signal'] = 0.0
    signals['Signal'] = np.where(
        data['Close'] < rolling_mean - 2 * rolling_std, 1.0, 0.0
    )
    signals['Signal'] = np.where(
        data['Close'] > rolling_mean + 2 * rolling_std, -1.0, signals['Signal']
    )
    signals['Positions'] = signals['Signal'].diff()
    
    return signals
