import random

ale = random.randint(1, 20)
print(ale)
num = int

while num != ale:
    num = int(input("Adivinhe um número aleatório: "))
    if num == ale:
        print("Você acertou o número")

    else:
        print("Você errou!")

print("Fim do jogo")
