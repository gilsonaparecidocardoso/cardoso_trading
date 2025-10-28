"""22. Value Investing
Value investing involves selecting stocks that appear to be trading for less than their intrinsic or book value.

It emphasizes long-term investment.
"""

def value_investing(stock_price, intrinsic_value):
    if stock_price < intrinsic_value * 0.8: # Buying at 80% of intrinsic value as an example
        return "buy"
    else:
        return "hold"