"""
Nome: Rafael fortunato Dametto
Curso: Tecnologia em Inteligência Artificial Aplicada
"""

"""Variáveis globais"""

estudantes = {}
adicionar_mais = -1
aluno = []


def menu_sistema_principal():
    """_Função de menu de navegação do sistema_"""
    opcao = -1
    while opcao != 0:
        opcao = int(
            input(
                """
====================Sistema de gestão de Dados Acadêmicos=====================
==============================================================================

=============================Menu - Navegação=================================
[0] Exit [1] Estudantes [2] Disciplinas [3] Professor [4] Turma [5] Matrícula
==============================================================================
    """
            )
        )

        if opcao == 1:
            menu_secundario(opcao=1)
        elif opcao == 2:
            menu_secundario(opcao=2)
        elif opcao == 3:
            menu_secundario(opcao=3)
        elif opcao == 4:
            menu_secundario(opcao=4)
        elif opcao == 5:
            menu_secundario(opcao=5)
        elif opcao < 0 or opcao > 5:
            print("Opção inválida")
        elif opcao == 0:
            print("Saindo...")

    else:
        print("Saindo do Sistema")


def menu_secundario(opcao):
    """Função secundária do menu recebe como parâmetro o nome da escolha"""
    if opcao == 1:
        menu_nome = "Estudante"
    elif opcao == 2:
        menu_nome = "Disciplinas em Desenvolvimento"
    elif opcao == 3:
        menu_nome = "Professor em Desenvolvimento"
    elif opcao == 4:
        menu_nome = "Turma em Desenvolvimento"
    else:
        menu_nome = "Matrícula em Desenvolvimento"

    caso = -1
    while caso != 0:
        caso = int(
            input(
                f"""
====================Sistema de gestão de Dados Acadêmicos======================
===============================================================================

                    Menu - {menu_nome}
            [0] Voltar [1] Incluir [2] Listar [3] Atualizar [4] Excluir
===============================================================================
    """
            )
        )
        if caso == 1:
            if menu_nome == "Estudante":
                cadastro_estudantes()
            else:
                print(f"Inserir {menu_nome} está em Desenvolvimento")
        elif caso == 2:
            if menu_nome == "Estudante":
                listar_estudantes()
            else:
                print(f"Listar {menu_nome} está em Desenvolvimento")
        elif caso == 3:
            if menu_nome == "Estudante":
                atualizar_aluno()
            else:
                print(f"Atualizar {menu_nome} está em Desenvolvimento")
        elif caso == 4:
            if menu_nome == "Estudante":
                exclui_aluno()
        elif caso < 0 or opcao >= 5:
            print("Opção inválida")
        elif caso == 0:
            print("Voltando...")
    else:
        print("Voltando ao menu principal")


def cadastro_estudantes():
    """_Função que grava o nome do estudante na lista_"""
    while True:
        # cria as variáveis nome, ra, e email e as solicita
        codigo = input(
            """
===========Inserindo Estudante===========
Digite o RA do estudante: 
=========================================
"""
        )
        nome = input(
            """
===========Inserindo Estudante===========
Digite o Nome do estudante: 
=========================================
"""
        )
        email = input(
            """
===========Inserindo Estudante===========
Digite o Email do estudante: 
=========================================
"""
        )
        # cria um dcionário com os dados do estudante
        estudantes[codigo] = {"nome": nome, "CPF": email}
        while True:
            adicionar_mais = int(
                input(
                    """
===========Inserindo Estudante===========
    [0] Voltar [1] Adicionar estudante 
=========================================
"""
                )
            )
            if adicionar_mais < 0 or adicionar_mais > 1:
                print("Opção inválida. Tente novamente.")
            else:
                break
        if adicionar_mais == 0:
            print("Voltando...")
            break


def listar_estudantes():
    """_Função de Listagem de Alunos_"""
    if len(estudantes) == 0:
        print("Nenhum estudante cadastrado.")
    else:
        for chave, valor in estudantes.items():
            print(chave, valor)


def exclui_aluno():
    """_Esta função exclui o aluno do RA selecionado do dicinário_"""
    codigo_aluno = input("Digite o Ra do aluno a ser Excluido: ")
    # através do metodo pop() busca-se m aluno pela chave RA e o exclui,
    # caso o aluno não exista, o programa retorna "RA não encontrado"
    codigo_excluido = estudantes.pop(codigo_aluno, "")
    if codigo_excluido == "":
        print("RA não encontrado")
    else:
        print(f"O aluno {codigo_excluido} foi excluido com sucesso.")


def atualizar_aluno():
    """_Esta função atualiza o aluno do RA selecionado do dicinário_"""
    codigo = input(
        """
===========Inserindo Estudante===========
Digite o RA do estudante: 
=========================================
"""
    )
    # Pede o novo nome do aluno
    nome_novo = input(
        """
===========Inserindo Estudante===========
Digite o novo nome do estudante: 
=========================================
"""
    )
    # Pede o novo email do aluno
    cpf_novo = input(
        """
===========Inserindo Estudante===========
Digite o novo email estudante: 
=========================================
"""
    )
    # Atualiza através do metodo update()
    # o nome e o email do aluno sem alterar o RA
    estudantes[codigo].update({"nome": nome_novo, "CPF": cpf_novo})


menu_sistema_principal()  # Chamada da função principal do sistema
