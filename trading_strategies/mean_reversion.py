"""8. Mean Reversion
Mean reversion is based on the assumption that prices will revert back to their historical average or mean.
"""

def mean_reversion(prices, historical_mean):
    if prices[-1] > historical_mean:
        return "sell"
    elif prices[-1] < historical_mean:
        return "buy"
    else:
        return "hold"