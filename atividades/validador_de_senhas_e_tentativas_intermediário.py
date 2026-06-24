senha_correta = "1234"

for tentativa in range(3):
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso Permitido")
        break
else:
    print("Conta Bloqueada")