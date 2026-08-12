class Numero:
    def __init__(self, valor:int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor *= 2

    def __str__(self):
        return f"Tenho o valor {self.valor} dentro do obj. Numero."

class Texto:
    def __init__(self, txt:str = ""):
        self.texto = txt

    def dobrar(self):
        self.texto = self.texto + " " + self.texto

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do obj. Texto."

class Lista:
    def __init__(self, lista:list = []):
        self.valores = lista

    def dobrar(self):
        self.valores += self.valores

    def __str__(self):
        return f"Tenho os valores {self.valores} no obj. Lista."

class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f"O papel está {'dobrado' if self.dobrado else 'novo'}"
        #if self.dobrado:
        #   return "O papel ESTÁ dobrado."
        #else:
        #   return "O papel NÃO ESTÁ dobrado."

class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return f"Era uma casa muito engraçada."

# DUCK TYPING --------------------------------------------------------------

def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"Não foi possível dobra o objeto: {objeto.__class__.__name__}")