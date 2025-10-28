from trading_strategies.arbitrage import arbitrage
from trading_strategies.auxiliar.excecoes.excecao_valor import ValorInvalidoError, verificar_valor
from trading_strategies.auxiliar.prices import get_crypto_prices

def teste_arbitrage():
    criptos = ['bitcoin', 'ethereum', 'dogecoin']
    btc_ticker = get_crypto_prices(criptos, 'brl')
    if btc_ticker:
        for cripto, preco in btc_ticker.items():
            try:
                verificar_valor(preco['brl'])
                print(f"Preço de {cripto.capitalize()}: R$ {preco['brl']:.2f}")
            except ValorInvalidoError as e:
                print(f"Capturada exceção: {e}")
                raise ValorInvalidoError(e)
            
            assert arbitrage(preco['brl'], preco['brl']) != None