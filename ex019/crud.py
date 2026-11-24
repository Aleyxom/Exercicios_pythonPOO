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
    print("\n --- LISTAGEM COMPLETA DE PESSOAS CADASTRADAS --- ")
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("SELECT cod, nome, altura FROM pessoas ORDER BY nome;")
            primeiro = cur.fetchone() #pega primeiro registro da seleção
            if not primeiro:
                print("[AVISO] Nenhum resultado foi encontrado!")
                return True

            print(f"\n" + "=" * 45)
            print(f"{'CÓD':<6} {'NOME':<28} {'ALTURA':>8}")
            print(f"-" * 45)

            vcod, vnome, valtura = primeiro
            print(f"{vcod:<6} {vnome:<28} {valtura:>8}m")

            for vcod, vnome, valtura in cur:
                print(f"{vcod:<6} {vnome:<28} {valtura:>8}m")

            print(f"\n" + "=" * 45)
        return True
    except sqlite3.Error as erro:
        print(f"[ERRO] Falha ao acessar o banco: {erro}")
        return False

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    print(f" --- EXCLUSÃO DE PESSOAS --- ")
    #listar todos -------------------------------------------------------------------------------
    listar_pessoa()
    #--------------------------------------------------------------------------------------------
    #perguntar o ID da exclusão -----------------------------------------------------------------
    entrada_cod = input(f"Informe o código da pessoa a excluir: ").strip()
    if not entrada_cod.isdigit():
        print("[ERRO] Código inválido!")
        return False
    # -------------------------------------------------------------------------------------------
    #buscar se a pessoa existe ------------------------------------------------------------------
    vcod = int(entrada_cod)
    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("SELECT nome, altura FROM pessoas WHERE cod=?;", (vcod,))
            pessoa = cur.fetchone()

            if not pessoa:
                print(f"[ERRO] Pessoa com código '{vcod}' não encontrada.")
                return False

            vnome, valtura = pessoa
    # ---------------------------------------------------------------------------------------------
    #Mostrar os dados da pessoa--------------------------------------------------------------------
            print(f'\nEncontrei o registro {vnome} com {valtura:.2f}m de altura')
    # ---------------------------------------------------------------------------------------------
    #pedir confirmação ----------------------------------------------------------------------------
            conf = input("Tem certeza que deseja excluir? [S/N] ").strip().upper()
    #----------------------------------------------------------------------------------------------
    #caso ok, excluir pessoa ----------------------------------------------------------------------
            if conf != "S":
                print("[AVISO] Exclusão foi cancelada!")
                return True

            cur.execute("DELETE FROM pessoas WHERE cod=?;",(vcod,))
            print(f"[AVISO] Acabei de excluir os dados de {vnome}")
            return True
    #----------------------------------------------------------------------------------------------
    except sqlite3.Error as erro:
        print(f"[ERRO] Falha ao excluir: {erro}")

def buscar_pessoa_por_nome() -> bool:
    print(f" --- BUSCA DE PESSOA POR NOME --- ")

    termo = input("Digite o nome ou parte dele para a busca: ")
    if not termo:
        print("[AVISO] Nenhum termo foi informado!")
        return False

    try:
        with sqlite3.connect(NOME_BANCO) as db:
            cur = db.cursor()
            cur.execute("SELECT cod, nome, altura FROM pessoas WHERE nome LIKE ? ORDER BY nome;", (f"%{termo}%",))

            primeiro = cur.fetchone()  # pega primeiro registro da seleção
            if not primeiro:
                print("[AVISO] Nenhum resultado foi encontrado com '{termo}'")
                return True

            print(f"\n" + "=" * 45)
            print(f"{'CÓD':<6} {'NOME':<28} {'ALTURA':>8}")
            print(f"-" * 45)

            vcod, vnome, valtura = primeiro
            print(f"{vcod:<6} {vnome:<28} {valtura:>8}m")

            for vcod, vnome, valtura in cur:
                print(f"{vcod:<6} {vnome:<28} {valtura:>8}m")

            print(f"\n" + "=" * 45)
        return True

    except sqlite3.Error as erro:
        print(f"[ERRO] Falha ao buscar no banco: {erro}")
        return False

