from rich import print, inspect
from classesex005 import Aluno, Professor, Funcionario

a1 = Aluno("José", 17, "Informática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()

p1 = Professor("Samuel", 37, "Ling. Portuguesa", "Especialista")
p1.dar_aula()

f1 = Funcionario("Ana Paula", 29, "Atendimento", "Farmácia")
f1.fazer_aniversario()
f1.bater_ponto()

inspect(a1)
inspect(p1)
inspect(f1)
