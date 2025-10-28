"""2. Momentum Trading
Traders buy securities that have had high returns over the past three to twelve months and sell those with poor returns.

It’s designed to capitalize on the continuation of existing trends.
"""

def momentum_trading(prices, period=12):
    momentum = prices[-1] - prices[-period]
    if momentum > 0:
        return "buy"
    else:
        return "sell"