"""5. Day Trading
Day trading involves buying and selling securities within the same trading day, not holding any positions overnight.
"""

def day_trading(prices, start_time, end_time):
    if current_time() < end_time:
        # Simple strategy based on price change
        if prices[-1] > prices[-2]:
            return "buy"
        else:
            return "sell"
    else:
        return "close all positions"