"""24. Dividend Investing
Dividend investing involves buying stocks of companies that pay high dividends in order to receive regular income.
"""

def dividend_investing(dividend_yield, target_yield):
    if dividend_yield > target_yield:
        return "buy"
    else:
        return "hold"