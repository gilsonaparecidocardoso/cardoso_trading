"""14. Volume Weighted Average Price (VWAP) Trading
VWAP trading tries to execute orders at a volume-weighted average price to minimize market impact.

Large institutional investors often execute their trades via VWAP when entering or exiting a position, given they may be a significant part of their markets and want to avoid disrupting the market.

Also common when executives with large ownership shares of their company choose to sell.
"""

def vwap_trading(prices, volumes):
    vwap = np.sum(prices * volumes) / np.sum(volumes)
    if prices[-1] > vwap:
        return "sell"
    elif prices[-1] < vwap:
        return "buy"
    else:
        return "hold"