"""16. Contrarian Investing/Trading
Contrarian investing is a strategy where investors go against prevailing market trends.

They buy assets when they’re out of favor and sell when they become popular.
"""

def contrarian_investing(market_sentiment, asset_price):
    if market_sentiment == "very positive":
        return "sell"
    elif market_sentiment == "very negative":
        return "buy"
    else:
        return "hold"