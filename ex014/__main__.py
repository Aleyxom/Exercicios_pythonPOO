from Exercicios_pythonPOO.ex014.classes import *

def main():
    x = Analisador()

    x.analisar(3)
    x.analisar("Olá")
    x.analisar(8.5)
    x.analisar([1,2,3,4,2,1,3,5])

if __name__ == "__main__":
    main()