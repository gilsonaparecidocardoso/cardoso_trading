"""1. Trend Following
Trend following involves buying securities that are trending upwards and selling those trending downwards.
It assumes that the trends will continue and is indicative of an underlying, sustainable market shift.
"""

def trend_following(prices):
    if prices[-1] > prices[-2]: # If the price is trending upwards
        return "buy"
    elif prices[-1] < prices[-2]: # If the price is trending downwards
        return "sell"
    else:
        return "hold"