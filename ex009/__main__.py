from Exercicios.ex009.ex009 import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao("Pedro", "Matemática")
    av1.set_nota(7.4)
    inspect(av1, private=True)
    print(f"O aluno {av1.nome} tirou {av1.get_nota()} na disciplina: {av1.disciplina}")


if __name__ == "__main__":
    main()