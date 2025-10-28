import requests
from trading_strategies.auxiliar.excecoes.excecao_request import RequestError, verificar_request
from pycoingecko import CoinGeckoAPI

def get_crypto_prices(coin_ids, currency):
    """
    Obtém preços de criptomoedas da CoinGecko.
    :param coin_ids: Lista de IDs de criptomoedas (ex: 'bitcoin', 'ethereum').
    :param currency: Moeda de referência (ex: 'usd', 'brl').
    """
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(coin_ids),
        'vs_currencies': currency
    }
    try:
        response = requests.get(url, params=params)
        if response == None:            
            verificar_request(response)
        response.raise_for_status()  # Lança um erro para status HTTP ruins
        data = response.json()
        return data
    except RequestError as e:
        raise RequestError(e)
    
def get_cg_crypto_prices(coin_ids, currency):
    cg = CoinGeckoAPI()
    try:
        price_data = cg.get_price(ids=coin_ids, vs_currencies=currency)
        return price_data[coin_ids][currency]
    except Exception as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

# criptos = ['bitcoin', 'ethereum', 'dogecoin']
# valores = get_cg_crypto_prices(criptos, 'brl')
# for cripto, preco in valores.items():
#     print(f"Preço de {cripto.capitalize()}: R$ {preco['brl']:.10f}")

#while True: #depois de 5 chamadas gera erro: Erro ao obter dados: 429 Client Error: Too Many Requests for url: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cdogecoin&vs_currencies=brl
#    # Exemplo de uso
#    criptos = ['bitcoin', 'ethereum', 'dogecoin']
#    valores = get_crypto_prices(criptos, 'brl')
#
#    if valores:
#        for cripto, preco in valores.items():
#            print(f"Preço de {cripto.capitalize()}: R$ {preco['brl']:.2f}")
#    
#    time.sleep(0.5) # Pausa a execução por 10 segundos
