from Exercicios_pythonPOO.ex019.crud import *


def exibir_menu():
    print("\n" + "=" * 30)
    print("     SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Atualizar pessoa")
    print("4 - Excluir pessoa")
    print("5 - Busca por nome")
    print("0 - Sair")
    print("=" * 30)

def main():

    # cadastro_em_massa() #IMPORTANTE! execute apenas uma vez! #Já executado!

    if not criar_banco():
        print("Algo de errado aconteceu com o banco de dados!")
        raise SystemExit

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1": #cadastrar pessoa
                if not cadastrar_pessoa():
                    print("[ERRO] Não foi possível cadastrar a pessoa!")
            case "2": #listar pessoa
                if not listar_pessoa():
                    print("[ERRO] Não foi possível mostar a listagem!")
            case "3": # atualizar pessoa
                if not atualizar_pessoa():
                    print("[ERRO] Não foi possível atualizar o cadastro!")
            case "4": #excluir pessoa
                if not excluir_pessoa():
                    print("[ERRO] Não foi possível excluir o cadastro!")
            case "5": #buscar por nome
                if not buscar_pessoa_por_nome():
                    print("[ERRO] Não foi possível fazer essa busca!")
            case "0": #Sair do sistema
                print("Encerrando o sistema...")
                break

            case _: #caso nenhuma das opções acima seja escolhida
                print("[ERRO] Opção inválida! Escolha uma opção entre 0 e 5")

        input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()