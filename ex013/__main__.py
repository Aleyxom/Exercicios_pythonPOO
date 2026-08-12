from Exercicios_pythonPOO.ex013.classes import *

def main():
    p1 = Mae("Jussiara")
    p2 = Filho("Pedro")
    p3 = Filha("Mônica")

    p1.fazer_pudim()
    p1.fritar_coxinha()

    p2.fazer_pudim()
    p2.fritar_coxinha()

    p3.fazer_pudim()
    p3.fritar_coxinha()

if __name__ == "__main__":
    main()