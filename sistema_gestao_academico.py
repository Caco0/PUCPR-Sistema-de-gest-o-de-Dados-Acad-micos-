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
                cadastro_geral(
                    chamador_menu_secundario,
                    "Estudante",
                    "o código do Estudante",
                    "nome do Estudante",
                    "CPF",
                )
                grava_arquivos(chamador_menu_secundario, "estudantes")
            elif menu_nome == "Disciplinas":
                cadastro_geral(
                    chamador_menu_secundario,
                    "Disciplina",
                    "o código do Disciplina",
                    "nome da Disciplina",
                    "aplicável em qtos Cursos",
                )
                grava_arquivos(chamador_menu_secundario, "disciplinas")
            elif menu_nome == "Professor":
                cadastro_geral(
                    chamador_menu_secundario,
                    "Professor",
                    "o código do Professor",
                    "nome do Professor",
                    "responsável por qtas turmas",
                )
                grava_arquivos(chamador_menu_secundario, "professores")
            elif menu_nome == "Turma":
                cadastro_geral(
                    chamador_menu_secundario,
                    "Turma",
                    "o código do Turma",
                    "o tipo do Curso",
                    "o Nome do Curso",
                )
                grava_arquivos(chamador_menu_secundario, "turmas")
            else:
                cadastro_geral(
                    chamador_menu_secundario,
                    "Matrícula",
                    "o código Matrícula",
                    "o código do Estudante",
                    "está habilitado para bolsa?",
                )
                grava_arquivos(chamador_menu_secundario, "matriculas")
        elif caso == 2:
            if menu_nome == "Estudante":
                ler_arquivo("estudantes")
                listar_registros(chamador_menu_secundario, "Estudantes")
            elif menu_nome == "Disciplinas":
                ler_arquivo("disciplinas")
                listar_registros(chamador_menu_secundario, "Disciplinas")
            elif menu_nome == "Professor":
                ler_arquivo("professores")
                listar_registros(chamador_menu_secundario, "Professores")
            elif menu_nome == "Turma":
                ler_arquivo("turmas")
                listar_registros(chamador_menu_secundario, "Turmas")
            else:
                ler_arquivo("matriculas")
                listar_registros(chamador_menu_secundario, "Matriculas")
        elif caso == 3:
            if menu_nome == "Estudante":
                atualizar_registros(
                    chamador_menu_secundario,
                    "código do Estudante",
                    "nome do Estudante",
                    "CPF",
                )
                grava_arquivos(chamador_menu_secundario, "estudante")
            elif menu_nome == "Disciplinas":
                atualizar_registros(
                    chamador_menu_secundario,
                    "código do Disciplina",
                    "nome da Disciplina",
                    "aplicável em qtos Cursos",
                )
                grava_arquivos(chamador_menu_secundario, "disciplinas")
            elif menu_nome == "Professor":
                atualizar_registros(
                    chamador_menu_secundario,
                    "código do Professor",
                    "nome do Professor",
                    "responsável por qtas turmas",
                )
                grava_arquivos(chamador_menu_secundario, "professor")
            elif menu_nome == "Turma":
                atualizar_registros(
                    chamador_menu_secundario,
                    "código do Turma",
                    "tipo do Curso",
                    "Nome do Curso",
                )
                grava_arquivos(chamador_menu_secundario, "turma")
            else:
                atualizar_registros(
                    chamador_menu_secundario,
                    "código Matrícula",
                    "código do Estudante",
                    "está habilitado para bolsa?",
                )
                grava_arquivos(chamador_menu_secundario, "matricula")
        elif caso == 4:
            if menu_nome == "Estudante":
                exclui_registros(chamador_menu_secundario, "Estudante")
            elif menu_nome == "Disciplinas":
                exclui_registros(chamador_menu_secundario, "Diciplina")
            elif menu_nome == "Professor":
                exclui_registros(chamador_menu_secundario, "Professor")
            elif menu_nome == "Turma":
                exclui_registros(chamador_menu_secundario, "Turma")
            else:
                exclui_registros(chamador_menu_secundario, "Matricula")
        elif caso < 0 or caso >= 5:
            print("Opção inválida")
        elif caso == 0:
            print("saindo...")
            break
        else:
            print("Você digitou uma opção inválida")
    return chamador_menu_secundario


def cadastro_geral(
    chamador_menu_secundario,
    nome_novo,
    texto1,
    texto2,
    texto3,
):
    """_Função que grava o nome do estudante na lista_"""
    while True:
        # cria as variáveis nome, ra, e email e as solicita
        try:
            codigo = int(
                input(
                    f"""
===========Inserindo {nome_novo}===========
Digite {texto1}: 
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
            f"""
===========Inserindo {nome_novo}===========
Digite {texto2}: 
=========================================
"""
        )
        cpf = input(
            f"""
===========Inserindo {nome_novo}===========
Digite {texto3}: 
=========================================
"""
        )
        # cria um dcionário com os dados do estudante
        chamador_menu_secundario[codigo] = {texto2: nome, texto3: cpf}
        while True:
            adicionar_mais = int(
                input(
                    f"""
===========Inserindo {nome_novo}===========
    [0] Voltar [1] Adicionar {nome_novo} 
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


def listar_registros(chamador_menu_secundario, nome_opção):
    """_Função de Listagem de Alunos_"""
    if len(chamador_menu_secundario) == 0:
        print("Nenhum estudante cadastrado na memória: ")
    else:
        for chave, valor in chamador_menu_secundario.items():
            print(f"{nome_opção} na memória{chave}, {valor}")


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


def atualizar_registros(chamador_menu_secundario, nome_novo, texto1, texto2, texto3):
    """_Esta função atualiza o aluno do RA selecionado do dicinário_"""
    while True:
        try:
            codigo = int(
                input(
                    f"""
        ===========Inserindo {nome_novo}===========
        Digite o {texto1}: 
        =========================================
        """
                )
            )
        except:
            print("Erro somente números são permitidos")
            # Pede o novo nome do aluno
            continue
        nome = input(
            f"""
    ===========Inserindo {nome_novo}===========
    Digite o novo {texto2}: 
    =========================================
    """
        )
        # Pede o novo email do aluno
        cpf = input(
            f"""
    ===========Inserindo {nome_novo}===========
    Digite o novo {texto3}: 
    =========================================
    """
        )
        # Atualiza através do metodo update()
        # o nome e o email do aluno sem alterar o RA
        chamador_menu_secundario[codigo].update({texto2: nome, texto3: cpf})
        break


def grava_arquivos(chamador_menu_secundario, file):
    """_Esta função grava o dicionário em um arquivo estudantes.json_"""
    with open(file + ".json", "w", encoding="utf-8") as f:
        json.dump(chamador_menu_secundario, f, ensure_ascii=False, indent=4)
        f.close()


def ler_arquivo(arquivo):
    """_Esta função lê o arquivo estudantes.json_"""
    estudantes_arquivados = {}
    try:
        with open(arquivo + ".json", "r") as f:
            estudantes_arquivados = json.load(f)
            f.close()
            print(estudantes_arquivados)
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
