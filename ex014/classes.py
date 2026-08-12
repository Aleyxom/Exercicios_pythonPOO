from functools import singledispatchmethod #pacote para fazer o polimorfismo sobrecarga
# existe a biblioteca externa multipledispatchmethod

class Analisador:

    @singledispatchmethod #metodo principal
    def analisar(self, valor):
        print(f"Não foi possível analisar o valor {valor}")

    @analisar.register #opção 1
    def _(self, valor:int):
        print(f"Valor {valor} é um número inteiro.")

    @analisar.register #opção 2
    def _(self, valor:str):
        print(f"Valor '{valor}' é uma cadeia de caracteres.")

    @analisar.register
    def _(self, valor:tuple|list|dict):
        print(f"Valor {valor} é uma coleção de dados.")

    @analisar.register
    def _(self, valor: float):
        print(f"Valor {valor} é uma número com ponto flutuante.")