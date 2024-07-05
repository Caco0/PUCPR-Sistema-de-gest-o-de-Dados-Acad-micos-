"""
Nome: Rafael fortunato Dametto
Curso: Tecnologia em Inteligência Artificial Aplicada
"""

import json


def menu_secundario(opcao):
    """Função secundária do menu recebe como parâmetro o nome da escolha"""
    if opcao == 1:
        menu_nome = "Estudante"
        chamador_menu_secundario = estudantes
    elif opcao == 2:
        menu_nome = "Disciplinas"
        chamador_menu_secundario = disciplinas
    elif opcao == 3:
        menu_nome = "Professor"
        chamador_menu_secundario = professores
    elif opcao == 4:
        menu_nome = "Turma"
        chamador_menu_secundario = turmas
    else:
        menu_nome = "Matrícula"
        chamador_menu_secundario = matriculas

    while True:
        try:
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
        except:
            print("Apenas números de 0 a 5 são permitidos")
            continue

        if caso == 1:
            if menu_nome == "Estudante":
                cadastro_geral(chamador_menu_secundario)
            elif menu_nome == "Disciplinas":
                cadastro_geral(chamador_menu_secundario)
            elif menu_nome == "Professor":
                cadastro_geral(chamador_menu_secundario)
            elif menu_nome == "Turma":
                cadastro_geral(chamador_menu_secundario)
            else:
                cadastro_geral(chamador_menu_secundario)
        elif caso == 2:
            if menu_nome == "Estudante":
                listar_registros(chamador_menu_secundario)
            elif menu_nome == "Disciplinas":
                listar_registros(chamador_menu_secundario)
            elif menu_nome == "Professor":
                listar_registros(chamador_menu_secundario)
            elif menu_nome == "Turma":
                listar_registros(chamador_menu_secundario)
            else:
                listar_registros(chamador_menu_secundario)
        elif caso == 3:
            if menu_nome == "Estudante":
                atualizar_registros(chamador_menu_secundario)
            elif menu_nome == "Disciplinas":
                atualizar_registros(chamador_menu_secundario)
            elif menu_nome == "Professor":
                atualizar_registros(chamador_menu_secundario)
            elif menu_nome == "Turma":
                atualizar_registros(chamador_menu_secundario)
            else:
                atualizar_registros(chamador_menu_secundario)
        elif caso == 4:
            if menu_nome == "Estudante":
                exclui_registros(chamador_menu_secundario)
            elif menu_nome == "Disciplinas":
                exclui_registros(chamador_menu_secundario)
            elif menu_nome == "Professor":
                exclui_registros(chamador_menu_secundario)
            elif menu_nome == "Turma":
                exclui_registros(chamador_menu_secundario)
            else:
                exclui_registros(chamador_menu_secundario)
        elif caso < 0 or caso >= 5:
            print("Opção inválida")
        elif caso == 0:
            print("saindo...")
            break
        else:
            print("Você digitou uma opção inválida")
    return chamador_menu_secundario


def cadastro_geral(chamador_menu_secundario):
    """_Função que grava o nome do estudante na lista_"""
    while True:
        # cria as variáveis nome, ra, e email e as solicita
        try:
            codigo = int(
                input(
                    """
===========Inserindo Registro===========
Digite o Código do estudante: 
=========================================
"""
                )
            )
        except:
            print("Erro somente números são permitidos")
            continue

        if codigo in chamador_menu_secundario:
            print("Código já cadastrado")
            print("Voltando ao Menu Estudante...")
            break
        nome = input(
            """
===========Inserindo Estudante===========
Digite o Nome do estudante: 
=========================================
"""
        )
        cpf = input(
            """
===========Inserindo Estudante===========
Digite o CPF do estudante: 
=========================================
"""
        )
        # cria um dcionário com os dados do estudante
        chamador_menu_secundario[codigo] = {"Nome": nome, "CPF": cpf}
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
            # grava_arquivo_estudantes(estudantes, "estudantes")
            break


def listar_registros(chamador_menu_secundario):
    """_Função de Listagem de Alunos_"""
    if len(chamador_menu_secundario) == 0:
        print("Nenhum estudante cadastrado na memória: ")
    else:
        for chave, valor in chamador_menu_secundario.items():
            print(f"Estudantes na memória{chave}, {valor}")

    # lista_de_estudantes = ler_arquivo_estudantes("estudantes")
    # print(f"Estudantes salvos: \n{lista_de_estudantes}")


def exclui_registros(chamador_menu_secundario):
    """_Esta função exclui o aluno do RA selecionado do dicinário_"""
    codigo_aluno = int(input("Digite o Ra do aluno a ser Excluido: "))
    # através do metodo pop() busca-se m aluno pela chave RA e o exclui,
    # caso o aluno não exista, o programa retorna "RA não encontrado"
    codigo_excluido = chamador_menu_secundario.pop(codigo_aluno, "")
    if codigo_excluido == "":
        print("Código não encontrado")
    else:
        print(f"O aluno {codigo_excluido} foi excluido com sucesso.")


def atualizar_registros(chamador_menu_secundario):
    """_Esta função atualiza o aluno do RA selecionado do dicinário_"""
    while True:
        try:
            codigo = int(
                input(
                    """
        ===========Inserindo Estudante===========
        Digite o Código do estudante: 
        =========================================
        """
                )
            )
        except:
            print("Erro somente números são permitidos")
            # Pede o novo nome do aluno
            continue
        nome_novo = input(
            """
    ===========Inserindo Estudante===========
    Digite o novo Nome do estudante: 
    =========================================
    """
        )
        # Pede o novo email do aluno
        cpf_novo = input(
            """
    ===========Inserindo Estudante===========
    Digite o novo CPF estudante: 
    =========================================
    """
        )
        # Atualiza através do metodo update()
        # o nome e o email do aluno sem alterar o RA
        chamador_menu_secundario[codigo].update({"Nome": nome_novo, "CPF": cpf_novo})
        break


def grava_arquivo_estudantes(estudantes, file):
    """_Esta função grava o dicionário em um arquivo estudantes.json_"""
    with open(file + ".json", "w", encoding="utf-8") as f:
        json.dump(estudantes, f, ensure_ascii=False, indent=4)
        f.close()


def ler_arquivo_estudantes(estudantes):
    """_Esta função lê o arquivo estudantes.json_"""
    estudantes_arquivados = {}
    try:
        with open(estudantes + ".json", "r") as f:
            estudantes_arquivados = json.load(f)
            f.close()
            return estudantes_arquivados
    except FileNotFoundError:
        print("Arquivo não encontrado")


"""Variáveis globais"""

estudantes = {}
disciplinas = {}
professores = {}
turmas = {}
matriculas = {}
adicionar_mais = -1
aluno = []


def menu_sistema_principal():
    """_Função de menu de navegação do sistema_"""
    while True:
        try:
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
        except:
            print("Opção inválida, tente novamente!")
            continue
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
            break
        else:
            print("Saindo do Sistema")


menu_sistema_principal()  # Chamada da função principal do sistema
