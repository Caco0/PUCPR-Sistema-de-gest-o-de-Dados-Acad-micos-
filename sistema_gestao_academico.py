def menu_sistema_principal():
    opcao = -1
    while opcao != 0:
        opcao = int(
            input(
                """
    ====================Sistema de gestão de Dados Acadêmicos======================
    ===============================================================================

    =============================Menu - Navegação==================================
     [0] Exit [1] Estudantes [2] Disciplinas [3] Professor [4] Turma [5] Matrícula
    ===============================================================================
    """
            )
        )

        if opcao == 1:
            estudantes(opcao=1)
        elif opcao == 2:
            estudantes(opcao=2)
        elif opcao == 3:
            estudantes(opcao=3)
        elif opcao == 4:
            estudantes(opcao=4)
        elif opcao == 5:
            estudantes(opcao=5)
        elif opcao < 0 or opcao > 5:
            print("Opção inválida")
        elif opcao == 0:
            print("Saindo...")

    else:
        print("Saindo do Sistema")


def estudantes(opcao):
    if opcao == 1:
        menu_nome = "Estudante"
    elif opcao == 2:
        menu_nome = "Disciplinas"
    elif opcao == 3:
        menu_nome = "Professor"
    elif opcao == 4:
        menu_nome = "Turma"
    else:
        menu_nome = "Matrícula"

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
            print(f"Incluir {menu_nome}")
        elif caso == 2:
            print(f"Listar {menu_nome}")
        elif caso == 3:
            print(f"Atualizar {menu_nome}")
        elif caso == 4:
            print(f"Excluir {menu_nome}")
        elif caso < 0 or opcao >= 5:
            print("Opção inválida")
        elif caso == 0:
            print("Saindo...")
    else:
        print("Voltando ao menu principal")


menu_sistema_principal()
