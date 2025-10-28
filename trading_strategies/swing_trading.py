"""3. Swing Trading
Swing traders capitalize on swings or fluctuations in asset prices over short to medium terms.

It strives to capture gains in a stock within an overnight to several weeks timeframe.
"""

def swing_trading(prices):
    # Simple example based on moving averages
    short_term = np.mean(prices[-5:])
    long_term = np.mean(prices[-20:])
    if short_term > long_term:
        return "buy"
    else:
        return "sell"