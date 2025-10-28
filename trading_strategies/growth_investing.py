"""23. Growth Investing
Growth investing focuses on companies expected to grow at an above-average rate compared to their industry or the overall market.
"""

def growth_investing(current_growth_rate, expected_growth_rate):
    if current_growth_rate > expected_growth_rate:
        return "buy"
    else:
        return "hold"