estudantes = {
    "rafael@gmail.com": {"nome": "Rafael", "ra": "3333-2221"},
    "maria@gmail.com": {"nome": "Maria", "ra": "3443-2121"},
    "jose@gmail.com": {"nome": "Jose", "ra": "3344-9871"},
    "churrupito@gmail.com": {"nome": "Churrupito", "ra": "3333-7766"},
}
adicionar_mais = -1


def cadastro_estudantes():
    while True:
        estudantes["nome"] = input("Digite o Nome do estudante: ")
        estudantes["ra"] = input("Digite o RA do estudante: ")
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
