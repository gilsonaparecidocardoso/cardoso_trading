"""18. Carry Trade
In a carry trade, an investor borrows money at a low interest rate and invests in an asset that provides a higher return.

They profit from the interest rate differential.
"""
 
def carry_trade(borrow_rate, investment_rate):
    if investment_rate > borrow_rate:
        return "borrow and invest"
    else:
        return "do not engage"