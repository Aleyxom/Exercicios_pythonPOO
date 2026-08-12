class Porta:
    def abrir(self):
        print("Girar a maçaneta e empurrar/puxar porta.")

class Empresa:
    def abrir(self):
        print("Vá ao portal do empreendedor com a doc. para abrir um cnpj.")

class Ovo:
    def abrir(self):
        print("Quebre a casca e separe as partes.")

class Pedra:
    pass

# METODO PYTHONICO POLIMORFICO DUCK TYPING
def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir {objeto.__class__.__name__}")