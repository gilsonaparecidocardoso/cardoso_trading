"""4. Scalping
Scalping involves making very rapid trades to capture small price changes, often entering and exiting trades within minutes.
"""

def scalping(prices, target_profit, stop_loss):
    buy_price = prices[-1]
    # Assume price changes
    current_price = get_current_price()
    if current_price - buy_price >= target_profit:
        return "sell"
    elif buy_price - current_price >= stop_loss:
        return "sell"
    else:
        return "hold"