# Declaração de classes
class Gafanhoto:
    """
    Essa classe cria um gafanhoto. Que é uma pessoa com nome e idade
    -Para criar, use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "vazio", idade = 0): # método construtor
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade!"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

    # Métodos de instância
    def aniversario(self):#quando a func. aniversario for chamada, mais um ano é acrescentado.
        self.idade += 1


# Declaração de objetos

g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)

g2 = Gafanhoto("Mauro", 20)
g2.aniversario()
print(g2)

g3 = Gafanhoto()
print(g3)

#print(g1.__doc__) # Dunder atributo
print(g1)
print(g1.__dict__) # atributo
print(g1.__getstate__()) # método, pois tem parenteses
print(g1.__class__)