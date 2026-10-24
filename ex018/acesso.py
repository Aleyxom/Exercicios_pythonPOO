import sqlite3

busca = str(input("Quem você está procurando? ")).strip()

try: #boas práticas

    with sqlite3.connect("meuBanco.db") as banco:
        banco.row_factory = sqlite3.Row #serve para ao inves do [0] poder usar o nome da coluna.
        cur = banco.cursor()
        #cur.execute("SELECT * FROM amigos") -> busca tudo da tabela
        #cur.execute(f"select * from amigos where nome LIKE '%{busca}%'") - funciona, mas é a forma errada: risco de SQL injection
        cur.execute("select * from amigos where nome LIKE ?", (f"%{busca}%",)) #forma mais segura

        # lista = cur.fetchall() -> pega tudo e joga na memoria principal, gasta memória
        # lista = cur.fetchone() # pega apenas 1

        total = 0

        for total, amigo in enumerate(cur, start=1):
            print(f"{amigo['nome']} nasceu em {amigo['nascimento']}")

        if total == 0:
            print(f"Não encontrei nenhum registro com: '{busca}'")
        else:
            print(f"Encontrei {total} resultados com '{busca}'")


except sqlite3 as erro:
    print(f"Falha no banco: {erro}")

except Exception as erro:

    print(f"Algo deu errado! {erro}")


# com o with no final ele encerra automaticamente o banco de dados após o uso.
#cur.close()
#banco.close()

# DESAFIO #
# Adapte o código do exercício para que a saída do script:

# mostre uma msg caso não seja achado nenhum registro. FEITO
# trate as datas inválidas e vazias.
# mostre a data formatada corretamente.
# mostre a idade real da pessoa.




