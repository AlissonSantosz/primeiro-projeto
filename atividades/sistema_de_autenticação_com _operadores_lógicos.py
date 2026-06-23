usuario = input("Digite o nome de usuário: ")
token = int(input("Digite o token de segurança: "))

if usuario == "admin" and token == 9988:
    print("Acesso concedido")

else:
    print("Dados de acesso inválidos")
