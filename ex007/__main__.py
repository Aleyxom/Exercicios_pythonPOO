from rich import print, inspect
from classes import Aluno, Professor, Funcionario, Pessoa

def main():
    a1 = Aluno("José", 17, "Informática", "T02")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()

    p1 = Professor("Samuel", 37, "Ling. Portuguesa", "Especialista")
    p1.dar_aula()
    p1.estudar()

    f1 = Funcionario("Ana Paula", 29, "Atendimento", "Farmácia")
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()

    x = Aluno("Aleyxom", 31, "TI", "SL01")
    x.fazer_aniversario()

    inspect(x, methods=True)

#inspect(a1)
#inspect(p1)
#inspect(f1)

if __name__ == "__main__":
    main()
