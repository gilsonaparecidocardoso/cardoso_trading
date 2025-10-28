"""20. Martingale System
The Martingale system involves doubling down on investments after losses, under the assumption that a winning bet will eventually occur and offset the losses.
"""

def martingale(bet_size, is_previous_bet_lost):
    if is_previous_bet_lost:
        return bet_size * 2
    else:
        return bet_size