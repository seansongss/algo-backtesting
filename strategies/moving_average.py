import pandas as pd
import numpy as np
from config import SHORT_WINDOW, LONG_WINDOW

def moving_average_strategy(data):
    data['SMA_Short'] = data['Close'].rolling(window=SHORT_WINDOW).mean()
    data['SMA_Long'] = data['Close'].rolling(window=LONG_WINDOW).mean()
    
    signals = pd.DataFrame(index=data.index)
    signals['Signal'] = 0.0
    signals['Signal'][SHORT_WINDOW:] = np.where(
        data['SMA_Short'][SHORT_WINDOW:] > data['SMA_Long'][SHORT_WINDOW:], 1, 0
    )
    signals['Positions'] = signals['Signal'].diff()

    return signals
