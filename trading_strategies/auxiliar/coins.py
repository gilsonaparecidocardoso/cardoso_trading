from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

# Faz a chamada para o endpoint /coins/list
# Isso retorna uma lista de dicionários, onde cada dicionário representa uma moeda.
def get_coins_list():
    try:
        coin_list = cg.get_coins_list(include_platform=True)

        if(coin_list):
            return coin_list

        ## Imprime as primeiras 20000 moedas para exemplo
        #print("Primeiras 20000 moedas disponíveis na CoinGecko API:")
        #print("--------------------------------------------------")
        #for coin in coin_list[:20000]:
        #    print(f"ID: {coin['id']}, Símbolo: {coin['symbol']}, Nome: {coin['name']}, Plataformas: {coin['platforms']}")
    #
        ## Para ver o número total de moedas, você pode usar a função len()
        #print(f"\nTotal de moedas disponíveis: {len(coin_list)}")

    except Exception as e:
        print(f"Ocorreu um erro ao conectar-se à CoinGecko API: {e}")
        return None