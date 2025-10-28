"""15. Dollar-Cost Averaging (DCA)
DCA involves regularly investing a fixed amount of money regardless of the asset’s price.

This reduces the impact of volatility.
"""

def dollar_cost_averaging(investment, current_price):
    # Calculate the number of shares to buy based on fixed investment amount
    shares = investment / current_price
    return shares