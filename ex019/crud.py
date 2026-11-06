import sqlite3

NOME_BANCO = "cadastro.db"

def criar_banco() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("")
        return True
    except sqlite3.Error as erro:
        print(f"Falha na criação do banco de dados: {erro}")
        return False
