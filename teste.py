estudantes = ["Rafael"]
adicionar_mais = -1


def cadastro_estudantes():
    while True:
        estudantes.append(input("Digite o nome do estudante: "))
        while True:
            adicionar_mais = int(input("[0] Voltar [1] Adicionar estudante "))
            if adicionar_mais < 0 or adicionar_mais > 1:
                print("Opção inválida. Tente novamente.")
            else:
                break
        if adicionar_mais == 0:
            print("Voltando...")
            break


def listar_estudantes():

    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
    else:
        for item in estudantes:
            print(item)


listar_estudantes()
cadastro_estudantes()
