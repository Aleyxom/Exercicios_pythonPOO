from abc import ABC, abstractmethod  # Abstract Base Class

class Pessoa(ABC):
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa): #subclasse de pessoa
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} foi matriculado!")

    def estudar(self):
        print(f"O {self.nome} está estudando {self.curso} na classe {self.turma}")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Prof. {self.nome} deu aula!")

    def estudar(self):
        print(f"O Prof. {self.nome} é {self.nivel} em {self.especialidade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu ponto agora!")

    def estudar(self):
        print(f"O funcionário {self.nome} fez o curso preparatório para ser promovido!")