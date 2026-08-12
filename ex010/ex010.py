class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    #criando atributo validável
    @property
    def nota(self): #GETTER
        return self._nota

    @nota.setter
    def nota(self, valor): #SETTER
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida!")

    @nota.deleter
    def nota(self):
        pass #não deu exemplo
