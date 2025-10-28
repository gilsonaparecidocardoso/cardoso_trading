"""11. Pairs Trading (Relative Value)
Pairs trading is a market-neutral strategy that involves taking matching positions in two correlated securities – i.e., buying one and short-selling the other when their price movements diverge.
"""

def pair_trading(asset_a_price, asset_b_price, threshold):
    # Calculate the price ratio or difference
    ratio = asset_a_price / asset_b_price
    if np.abs(ratio - 1) > threshold:
        if ratio > 1:
            return "buy B, sell A"
        else:
            return "buy A, sell B"
    else:
        return "no action"