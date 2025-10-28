"""12. News Trading
News trading involves making trades based on news events, anticipating that the market will move significantly in response to news.
"""

def news_trading(news, current_price):
    if "positive" in news:
        return "buy"
    elif "negative" in news:
        return "sell"
    else:
        return "hold"