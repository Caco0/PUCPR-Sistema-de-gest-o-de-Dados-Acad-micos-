"""
Nome: Rafael Fortunato Dametto
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
        # chama o cadastro geral por setor e em seguida grava em seu
        # arquivo específico
        if caso == 1:
            if menu_nome == "Estudante":
                cadastro_geral(
                    chamador_menu_secundario,
                    "Estudante",
                    "Código do Estudante",
                    "Nome do Estudante",
                    "CPF",
                )
                grava_arquivos(chamador_menu_secundario, "estudantes")
            elif menu_nome == "Disciplinas":
                cadastro_geral(
                    chamador_menu_secundario,
                    "Disciplina",
                    "Código do Disciplina",
                    "Nome da Disciplina",
                    "aplicável em qtos Cursos",
                )
                grava_arquivos(chamador_menu_secundario, "disciplinas")
            elif menu_nome == "Professor":
                cadastro_geral(
                    chamador_menu_secundario,
                    "Professor",
                    "Código do Professor",
                    "Nome do Professor",
                    "CPF Professor",
                )
                grava_arquivos(chamador_menu_secundario, "professores")
            elif menu_nome == "Turma":
                cadastro_geral(
                    chamador_menu_secundario,
                    "Turma",
                    "Código do Turma",
                    "Código da Professor",
                    "Código da Disciplina",
                )
                grava_arquivos(chamador_menu_secundario, "turmas")
            else:
                cadastro_geral(
                    chamador_menu_secundario,
                    "Matrícula",
                    "Código Matrícula",
                    "Código do Estudante",
                    "Código da Turma",
                )
                grava_arquivos(chamador_menu_secundario, "matriculas")
        # Lê a memória listada por setor específico, e imprime o arquivo
        # gravado também por setor
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
        # Atualiza os registros por setor e em seguida grava novamente
        # no arquivo
        elif caso == 3:
            if menu_nome == "Estudante":
                atualizar_registros(
                    chamador_menu_secundario,
                    "Código do Estudante",
                    "Nome do Estudante",
                    "CPF",
                )
                grava_arquivos(chamador_menu_secundario, "estudantes")
            elif menu_nome == "Disciplinas":
                atualizar_registros(
                    chamador_menu_secundario,
                    "Código do Disciplina",
                    "Nome da Disciplina",
                    "aplicável em qtos Cursos",
                )
                grava_arquivos(chamador_menu_secundario, "disciplinas")
            elif menu_nome == "Professor":
                atualizar_registros(
                    chamador_menu_secundario,
                    "Código do Professor",
                    "Nome do Professor",
                    "CPF Professor",
                )
                grava_arquivos(chamador_menu_secundario, "professores")
            elif menu_nome == "Turma":
                atualizar_registros(
                    chamador_menu_secundario,
                    "Código do Turma",
                    "Código da Professor",
                    "Código da Disciplina",
                )
                grava_arquivos(chamador_menu_secundario, "turmas")
            else:
                atualizar_registros(
                    chamador_menu_secundario,
                    "Código Matrícula",
                    "Código do Estudante",
                    "Código da Turma",
                )
                grava_arquivos(chamador_menu_secundario, "matriculas")
        # seleciona através do código o registro a ser apagado, apaga
        # e imprime na tela o registro apagado
        elif caso == 4:
            if menu_nome == "Estudante":
                exclui_registros(chamador_menu_secundario, "Estudante")
                grava_arquivos(chamador_menu_secundario, "estudantes")
            elif menu_nome == "Disciplinas":
                exclui_registros(chamador_menu_secundario, "Disciplina")
                grava_arquivos(chamador_menu_secundario, "disciplinas")
            elif menu_nome == "Professor":
                exclui_registros(chamador_menu_secundario, "Professor")
                grava_arquivos(chamador_menu_secundario, "professores")
            elif menu_nome == "Turma":
                exclui_registros(chamador_menu_secundario, "Turma")
                grava_arquivos(chamador_menu_secundario, "turmas")
            else:
                exclui_registros(chamador_menu_secundario, "Matricula")
                grava_arquivos(chamador_menu_secundario, "matriculas")
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
    nome_novo,  # nome da opção escolhida para imprimir na tela
    texto1,  # primeira pergunta, segundo a OPÇÃO escolhida
    texto2,  # segunda pergunta, segundo a OPÇÃO escolhida
    texto3,  # terceira pergunta, segundo a OPÇÃO escolhida
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
        # cria um dicionário com os dados do estudante
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
    """_Esta função exclui o aluno do RA selecionado do dicionário_"""
    codigo_aluno = int(input("Digite o Ra do aluno a ser Excluido: "))
    # através do método pop() busca-se m aluno pela chave RA e o exclui,
    # caso o aluno não exista, o programa retorna "RA não encontrado"
    codigo_excluido = chamador_menu_secundario.pop(codigo_aluno, "")
    if codigo_excluido == "":
        print("Código não encontrado")
    else:
        print(f"O aluno {codigo_excluido} foi excluido com sucesso.")


def atualizar_registros(chamador_menu_secundario, nome_novo, texto1, texto2):
    """_Esta função atualiza o aluno do RA selecionado do dicionário_"""
    while True:
        try:
            codigo = int(
                input(
                    """
=============Inserindo Código============
Digite o Código: 
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
Digite o novo {texto1}: 
=========================================
    """
        )
        # Pede o novo email do aluno
        cpf = input(
            f"""
===========Inserindo {nome_novo}===========
Digite o novo {texto2}: 
=========================================
    """
        )
        # Atualiza através do método update()
        # o nome e o email do aluno sem alterar o RA
        chamador_menu_secundario[codigo].update({texto1: nome, texto2: cpf})
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
