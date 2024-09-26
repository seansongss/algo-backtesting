from strategies.moving_average import moving_average_strategy
from strategies.mean_reversion import mean_reversion_strategy

from config import STRATEGY

def get_signals(data):
    match STRATEGY:
        case 'moving_average':
            return moving_average_strategy(data)
        
        case 'mean_reversion':
            return mean_reversion_strategy(data)