from datetime import datetime
import sqlite3
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
        print("--------------------------------------------------")
        for coin in coin_list[:20000]:
            print(f"ID: {coin['id']}, Símbolo: {coin['symbol']}, Nome: {coin['name']}, Plataformas: {coin['platforms']}")
            insere_moeda({coin['symbol']}, {coin['name']}, {coin['platforms']}, None, datetime.now())
        
        ## Para ver o número total de moedas, você pode usar a função len()
        print(f"\nTotal de moedas disponíveis: {len(coin_list)}")

    except Exception as e:
        print(f"Ocorreu um erro ao conectar-se à CoinGecko API: {e}")
        return None

#Função para inserir os dados no banco de dados SQLite
def insere_moeda(symbol, name, platforms, currency, data):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    query = "INSERT INTO coins_moedas ( symbol, name, platforms, currency, data) " \
            f"VALUES (symbol = {symbol} ,name = {name} ,platforms = {platforms} ,currency = {currency} ,data = {data});"
    #cursor.execute("INSERT INTO leitor_pdf_leitor (data, num_cartao, estabelecimento, valor) VALUES (?, ?, ?, ?)", (data, numero, estabelecimento, valor))
    cursor.execute(query)
    conn.commit()
    conn.close()
#
#