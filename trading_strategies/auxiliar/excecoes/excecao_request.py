import requests

class RequestError(requests.exceptions.RequestException):
    def __init__(self, valor, mensagem="Erro ao obter dados"):
        self.valor = valor
        self.mensagem = f"{mensagem}: {valor}"
        super().__init__(self.mensagem)

def verificar_request(x):
    if x == None:
        raise RequestError(x)
    else:
        print("Request válido")