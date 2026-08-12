class Mae:
    def __init__(self, nome:str = "mamãe"):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com leite condensado e calda.")

    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha com oleo de soja")

class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz pudim com leite ninho e Nutella")

class Filho(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} frita coxinha na Airfryer")