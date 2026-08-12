from Exercicios.ex010.ex010 import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao("Pedro", "Matemática")
    av1.nota = 9.5
    inspect(av1, private=True)
    print(f"O aluno {av1.nome} tirou {av1.nota} na disciplina: {av1.disciplina}")


if __name__ == "__main__":
    main()