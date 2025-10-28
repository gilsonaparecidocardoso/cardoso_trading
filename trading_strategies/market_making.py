"""10. Market Making
Market makers provide liquidity in the markets by buying and selling securities to facilitate trading.

They earn profits on the bid-ask spread.
"""

def market_making(bid_price, ask_price, target_spread):
    if ask_price - bid_price > target_spread:
        return "place buy order at bid, sell order at ask"