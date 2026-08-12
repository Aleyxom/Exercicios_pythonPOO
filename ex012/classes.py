from abc import ABC, abstractmethod

# Polimorfismo DE INCLUSÃO OU OVERRIDE(sobrescreve) OU SUBTYPING - esse exemplo # o python tem esses dois
                                                                                # Duck Typing: aplicação do método
# Sobrecarga - Ad-Hoc Overload                                                  # polimórfico.
# Coerção - Ad-Hoc Coercion
# Paramétrico - Template - Genérico

class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está emitindo um som!")

class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} acabou de dizer 'QUACK QUACK'")


class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} acabou de dizer 'AU AU AU'")

class Spitz(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} acabou de dizer 'au! au! au! au! au! au! au!'")

class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} acabou de dizer 'RUF RUF'")

class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} acabou de dizer 'MIAAU'")

class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} acabou de dizer 'PÓ PÓ PÓ'")
