import sqlite3

NOME_BANCO = "cadastro.db"

def criar_banco() -> bool:
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS pessoas(cod INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, altura REAL NOT NULL);")

            #db.commit() confirma e salva, mas com o WITH já faz automatico.
            # db.rollback() cancela alteração, em caso de dar uma falha

            return True
    except sqlite3.Error as erro:
        print(f"Falha na criação do banco de dados: {erro}")
        return False

def cadastro_em_massa():
    cad_pessoas = [
        ("1", "Gustavo", "1.84"),
        ("2", "Gabriela", "1.63"),
        ("3", "Pedro", "2.02"),
        ("4", "Mariana", "1.72"),
    ]

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur =db.cursor()
            cur.executemany("INSERT INTO pessoas (cod, nome, altura) VALUES (?, ?, ?)", cad_pessoas)

    except sqlite3.Error as erro:
        print("[ERRO] Falha ao fazer cadastro em massa!")

def cadastrar_pessoa() -> bool:
    print("\n ==== NOVO CADASTRO DE PESSOA ==== ")

    # --------Leitura e validação dos dados ----------------------
    val_nome = input("Nome: ").strip()
    if not val_nome:
        print("[ERRO] O nome é um campo obrigatório!")
        return False

    val_altura = input("Altura (metros): ").strip().replace(",", ".")
    if not val_altura:
        print("[ERRO] Altura é um campo obrigatório!")
        return False

    try:
        altura = float(val_altura)
        if altura <= 0.30 or altura > 3.0:
            print("[ERRO] Valor incoerente para altura!")
            return False
    except ValueError:
        print("[ERRO] Altura precisa ser um número.")
        return False

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO pessoas (nome, altura) VALUES (?, ?)", (val_nome, val_altura))
            print(f"Cadastro de {val_nome} realizado com sucesso!")
            return True

    except sqlite3.Error as erro:
        print(f"[ERRO] Falha no cadastro do banco: {erro}")
        return False

def listar_pessoa() -> bool:
    pass

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    pass

def buscar_pessoa_por_nome() -> bool:
    pass

