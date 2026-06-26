import time
opcao1= int
opcao2 = int

while True:

    opcao = int(input("""
    MENU
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    5 - Sair
    Digite sua opção: """))

    if 1 <= opcao <= 4:
        opcao1 = float(input("Digite o primeiro número: "))
        opcao2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print("SOMAR", opcao1 + opcao2)
    elif opcao == 2:
        print("Subtrair", opcao1 - opcao2)
    elif opcao == 3:
        print("Multiplicar", opcao1 * opcao2)
    elif opcao == 4:
        print("Dividir", opcao1 / opcao2)
    elif opcao == 5:
        print("Saindo...")
        time.sleep(1)
        break
    else:
        print("Opção inválida, escolha uma nova")
