"""6. Position Trading
Position trading is a long-term strategy where traders hold positions for weeks to months or even years.

They focus on the asset’s long-term performance.

It’s essentially a hybrid between trading and investing.
"""

def position_trading(prices, long_term_trend):
    if long_term_trend == "up":
        return "buy and hold"
    elif long_term_trend == "down":
        return "sell or stay out"