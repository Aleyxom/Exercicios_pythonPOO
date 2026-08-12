from Exercicios_pythonPOO.ex015.classes import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(100)

    print(c1 == c2)
    c1 += 50
    print(c1 == c2)

    print(c1)
    print(c2)

    c2 -= 50

    print(c2)

    if c1 == c2:
        print("Vocês tem o mesmo valor na carteira.")
    else:
        print("Valores diferentes nas carteiras.")

    print(c2 <= c1)


if __name__ == "__main__":
    main()