from turtledemo.paint import switchupdown


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
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1": #cadastrar pessoa
                pass
            case "2": #listar pessoa
                pass
            case "3": # atualizar pessoa
                pass
            case "4": #excluir pessoa
                pass
            case "5": #buscar por nome
                pass
            case "0": #Sair do sistema
                print("Encerrando o sistema...")
                break

            case _: #caso nenhuma das opções acima seja escolhida
                print("[ERRO] Opção inválida! Escolha uma opção entre 0 e 5")

        input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()