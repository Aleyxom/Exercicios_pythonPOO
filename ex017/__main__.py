from Exercicios_pythonPOO.ex017.classes import *

def main():
    objetos = [Numero(200), Texto("Aleyxom"), Lista([1,2,3]), Papel(), Casa()]

    for objeto in objetos:
        tente_dobrar(objeto)
        print(objeto)

if __name__ == "__main__":
    main()