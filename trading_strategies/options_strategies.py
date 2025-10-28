"""17. Options Strategies (e.g., Covered Calls, Iron Condor)
Options strategies involve the use of options contracts to achieve various investment goals, like income generation, generating synthetic leverage, or prudent risk management.
"""

def covered_call(stock_price, strike_price, premium_received):
    # Example of a simple covered call strategy
    if stock_price > strike_price:
        return "exercise option, sell stock"
    else:
        return "keep premium"