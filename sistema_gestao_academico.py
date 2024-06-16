def menu_sistema_principal():
    print(
        """
    ====================Sistema de gestão de Dados Acadêmicos====================
    =============================================================================
"""
    )
    opcao = -1
    while opcao != 0:
        opcao = int(
            input(
                """
    =============================Menu - Navegação=================================
     [0] Exit [1] Estudantes [2] Disciplinas [3] Professor [4] Turma [5] Matrícula
    ==============================================================================
    """
            )
        )

        if opcao == 1:
            estudantes()
        elif opcao == 2:
            disciplinas()
        elif opcao == 3:
            professor()
        elif opcao == 4:
            turma()
        elif opcao == 5:
            matriculas()
        elif opcao < 0 or opcao > 5:
            print("Opção inválida")
        elif opcao == 0:
            print("Saindo...")

    else:
        print("Saindo do Sistema")


def estudantes():
    opcao = -1
    while opcao != 0:
        opcao = int(
            input(
                """
    ===================Menu - Estudante========================
     [0] Voltar [1] Incluir [2] Listar [3] Atualizar [4] Excluir
    ===========================================================
    """
            )
        )
        if opcao == 1:
            print("Incluir Estudantes")
        elif opcao == 2:
            print("Listar Estudantes")
        elif opcao == 3:
            print("Atualizar Estudantes")
        elif opcao == 4:
            print("Excluir Estudantes")
        elif opcao < 0 or opcao >= 5:
            print("Opção inválida")
        elif opcao == 0:
            print("Saindo...")
    else:
        print("Voltando ao menu principal")


def disciplinas():
    opcao = -1
    while opcao != 0:
        opcao = int(
            input(
                """
    ===================Menu - Disciplinas=======================
     [0] Voltar [1] Incluir [2] Listar [3] Atualizar [4] Excluir
    ===========================================================
    """
            )
        )
        if opcao == 1:
            print("Incluir Disciplina")
        elif opcao == 2:
            print("Listar Disciplina")
        elif opcao == 3:
            print("Atualizar Disciplina")
        elif opcao == 4:
            print("Excluir Disciplina")
        elif opcao < 0 or opcao >= 5:
            print("Opção Inválida")
        elif opcao == 0:
            print("Saindo do menu Disciplinas")
    else:
        print("Voltando ao menu Principal")


def professor():
    opcao = -1
    while opcao != 0:
        opcao = int(
            input(
                """
    ===================Menu - Professor========================
     [0] Voltar [1] Incluir [2] Listar [3] Atualizar [4] Excluir
    ===========================================================
    """
            )
        )
        if opcao == 1:
            print("Incluir Professor")
        elif opcao == 2:
            print("Listar Professor")
        elif opcao == 3:
            print("Atualizar Professor")
        elif opcao == 4:
            print("Excluir Professor")
        elif opcao < 0 or opcao >= 5:
            print("Opção inválida")
        elif opcao == 0:
            print("Saindo...")
    else:
        print("Voltando ao menu Principal")


def turma():
    opcao = -1
    while opcao != 0:
        opcao = int(
            input(
                """
    =====================Menu - Turma==========================
     [0] Voltar [1] Incluir [2] Listar [3] Atualizar [4] Excluir
    ===========================================================
    """
            )
        )
        if opcao == 1:
            print("Incluir Turma")
        elif opcao == 2:
            print("Listar Turma")
        elif opcao == 3:
            print("Atualizar Turma")
        elif opcao == 4:
            print("Excluir Turma")
        elif opcao < 0 or opcao >= 5:
            print("Opção inválida")
        elif opcao == 0:
            print("Saindo...")
    else:
        print("Voltando ao menu Principal")


def matriculas():
    opcao = -1
    while opcao != 0:
        opcao = int(
            input(
                """
    ====================Menu - Matrículas======================
     [0] Voltar [1] Incluir [2] Listar [3] Atualizar [4] Excluir
    ===========================================================
    """
            )
        )
        if opcao == 1:
            print("Incluir Matrículas")
        elif opcao == 2:
            print("Listar Matrículas")
        elif opcao == 3:
            print("Atualizar Matrículas")
        elif opcao == 4:
            print("Excluir Matrículas")
        elif opcao < 0 or opcao >= 5:
            print("Opção inválida")
        elif opcao == 0:
            print("Saindo...")
    else:
        print("Voltando ao menu principal")


menu_sistema_principal()
