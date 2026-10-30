from cadastro import CadastroAlunos


def exibir_menu():
    print("\n=== Sistema de Cadastro de Alunos | Projeto GCS ===")
    print("Gerenciamento de alunos - Versao academica")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Remover aluno")
    print("0. Sair")


def main():
    cadastro = CadastroAlunos()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome do aluno: ").strip()
            matricula = input("Matrícula: ").strip()
            try:
                cadastro.adicionar(nome, matricula)
                print("Aluno cadastrado com sucesso.")
            except ValueError as erro:
                print(f"Não foi possível cadastrar: {erro}")
        elif opcao == "2":
            alunos = cadastro.listar()
            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for aluno in alunos:
                    print(f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']}")
        elif opcao == "3":
            matricula = input("Matrícula do aluno a remover: ").strip()
            if cadastro.remover(matricula):
                print("Aluno removido com sucesso.")
            else:
                print("Matrícula não encontrada.")
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
