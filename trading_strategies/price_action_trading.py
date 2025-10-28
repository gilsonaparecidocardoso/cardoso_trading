"""21. Price Action Trading
Price action trading relies on historical price movements and patterns to make trading decisions without the use of indicators.
"""

def price_action_trading(price_history):
    # Simple example: buy if price breaks above previous high, sell if below previous low
    if price_history[-1] > max(price_history[:-1]):
        return "buy"
    elif price_history[-1] < min(price_history[:-1]):
        return "sell"
    else:
        return "hold"