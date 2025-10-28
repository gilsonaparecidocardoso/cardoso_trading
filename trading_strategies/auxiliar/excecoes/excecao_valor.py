class ValorInvalidoError(Exception):
    def __init__(self, valor, mensagem="O valor fornecido é inválido"):
        self.valor = valor
        self.mensagem = f"{mensagem}: {valor}"
        super().__init__(self.mensagem)

def verificar_valor(x):
    if x == None:
        raise ValorInvalidoError(x)
    else:
        print("Valor válido")