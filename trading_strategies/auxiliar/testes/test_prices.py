from trading_strategies.auxiliar.prices import get_crypto_prices

def teste_prices():
#    while True: #depois de 5 chamadas gera erro: Erro ao obter dados: 429 Client Error: Too Many Requests for url: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cdogecoin&vs_currencies=brl
        # Exemplo de uso
    criptos = ['bitcoin', 'ethereum', 'dogecoin']
    valores = get_crypto_prices(criptos, 'brl')
    assert valores != None

    if valores:
        for cripto, preco in valores.items():
            print(f"Preço de {cripto.capitalize()}: R$ {preco['brl']:.2f}")
        
#        time.sleep(0.5) # Pausa a execução por 10 segundos
