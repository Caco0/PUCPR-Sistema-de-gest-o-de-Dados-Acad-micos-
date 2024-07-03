while True:
    print("1. Doces")
    print("2. Salgados")
    print("3. Bebidas")
    print("4. Sair")
    try:
        opcao = int(input("Digite uma opção: "))
    except:
        print("Você digitou uma opção inválida. tente novamente!")
        continue

    if opcao >= 1 and opcao <= 3:
        print("Você escolheu a opção", opcao, ".")
    elif opcao == 4:
        print("Você escolheu sair")
        break
    else:
        print("Você digitou uma opção inválida. tente novamente!")
