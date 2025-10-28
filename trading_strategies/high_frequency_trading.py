"""7. High-Frequency Trading (HFT)
HFT is a type of algorithmic trading characterized by:

high speeds
high turnover rates, and
high order-to-trade ratios that leverages high-frequency financial data and electronic trading tools
"""

def high_frequency_trading(prices):
    # Example: arbitrage opportunity detection
    if prices['Exchange1'] < prices['Exchange2']:
        return "buy on Exchange1 and sell on Exchange2"
    else:
         return "hold"