from classes import Livro

# Lista pra armazenar os livros
biblioteca = []

# Menu principal
while True:
    print("-" * 10, "BIBLIOTECA", "-" * 10)
    print("MENU PRINCIPAL")
    print("1 - Cadastrar livro")
    print("2 - Consultar livros")
    print("3 - Remover livro")
    print("0 - Sair")

    opcao_menu = input("escolha uma opção: ")

    match (opcao_menu):
        case "1":
            while True:
                try:
                    id = int(input("Informe o ID do livro: "))

                #Tratamento de erros caso não digite um valor inteiro
                except ValueError:
                    print("Por favor, digite um número válido.")
                else:
                    autor = input("Digite o nome do autor: ")
                    nome = input("Digite o nome do livro: ")
                    editora = input("Informe a editora: ")
                    ano = input("Diga o ano de lançamento: ")

                    # Instanciando um objeto
                    livro = Livro(id,autor, nome, editora, ano)

                    # adicionando o livro à lista biblioteca
                    biblioteca.append(livro.add_livro())

                    novo_cadastro = input("Deseja fazer um novo cadastro? [Y/N] ")

                    if novo_cadastro in "Yy":
                        print("Iniciando novo cadastro.")
                        continue
                    elif novo_cadastro in "Nn":
                        print("Voltando para o menu principal...")
                        break
                    else:
                        print("Por favor, escolha uma opção do menu.")
                        break

        case "2":
            while True:
                # Menu consultar livros
                print("MENU CONSULTAR LIVROS")
                print("1 - Consultar todos os livros")
                print("2 - Consultar livro por ID:")
                print("0 - Voltar para o menu principal")

                opcao_consultar = input("Selecione uma opção: ")

                if opcao_consultar == "1":
                    for livro_consulta in biblioteca:
                        # Linha para separar os resultados
                        print("-" * 10)
                        for chave, valor in livro_consulta.items():
                            print(f"{chave}: {valor}")

                elif opcao_consultar == "2":
                    while True:
                        try:
                            consulta_id = int(input("Qual o ID do livro que deseja consultar? "))
                        except ValueError:
                            print("Por favor, digite um número inteiro.")
                        else:
                            # Verifica se o id escolhido está dentro dos valores do dicionário.
                            for id_livro in biblioteca:
                                if consulta_id in id_livro.values():
                                    # Mostra as informações do livro
                                    for chave_id, valor_id in id_livro.items():
                                        print(f"{chave_id}: {valor_id}")
                                else:
                                    print("O ID procurado não existe. Tente novamente.")
                                    break

                        # Pergunta se deseja fazer uma nova consulta
                        nova_consulta = input("Deseja fazer uma nova consulta? [Y/N] ")
                        if nova_consulta in "Yy":
                            continue
                        elif nova_consulta in "Nn":
                            print("Voltando para o menu de consulta de livros...")
                            break
                        else:
                            print("Por favor, escolha uma opção do menu.")
                            break

                elif opcao_consultar == "0":
                    print("Votlando para o menu principal...")
                    break
                else:
                    print("Digite um número válido")
                    continue
        case "3":
            escolher_indice = int(input("Escolha o índice do livro que deseja excluir: "))
            livro.remove_livro(biblioteca, escolher_indice)
            continue
        case "0":
            print("Encerrando o programa...")
            break
        case _:
            print("Por favor, escolha uma opção do menu.")

