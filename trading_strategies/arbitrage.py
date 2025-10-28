"""9. Arbitrage
Arbitrage involves simultaneously buying and selling an asset or equivalent assets to profit from price discrepancies across different markets or forms.
"""

def arbitrage(price_a, price_b):
    if price_a < price_b:
        return "compra A:" , price_a , ", vende B:" , price_b , '.'
    elif price_a > price_b:
        return "compre B:" , price_b , ", venda A:" , price_a , '.'
    elif price_a == price_b:
        return "sem oportunidade de arbitragem."
    else:
        return None

# criptos = ['bitcoin', 'ethereum', 'dogecoin']
# btc_ticker = get_crypto_prices(criptos, 'brl')
# if btc_ticker:
#     for cripto, preco in btc_ticker.items():
#         print(f"Preço de {cripto.capitalize()}: R$ {preco['brl']:.2f}")
#         print(arbitrage(preco['brl'], preco['brl']))