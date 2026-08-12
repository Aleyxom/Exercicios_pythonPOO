from Exercicios_pythonPOO.ex012.classes import *

def main():
    animais = [Cachorro("Scooby"), Gato("Pitubi"), Pato("Donald"), Galinha("Pintadinha"),
               Spitz("Lulu"), Pitbull("Brutus")]

    for animal in animais:
        animal.emitir_som()

if __name__ == "__main__":
    main()