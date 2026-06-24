n = 0
for i in range(1,8):
    i += 1
    ano = int(input("Digite seu ano de nascimento: "))
    idade = 2026 - ano

    if idade >= 18:
        n += 1

print(f"{n} pessoas alcançaram a maioridade")