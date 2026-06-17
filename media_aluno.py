nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota^: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Aluno(a) Aprovado(a) com media {media:.2f}")
elif media >= 3 and media < 7 :
    print(f"Aluno(a) em Recuperacao com media {media:.2f}")
    fez_recuperacao = input("Aluno já fez a recuperacao? s/n: ")
    if fez_recuperacao == "s" :
        nota_recuperacao = float(input("Digite a nota da recuperação: "))
        if nota_recuperacao >= 5:
            print("Aluno(a) aprovado pela recuperacao")
        else:
            print("Aluno(a) não obteve nota suficiente para ser aprovado após a recuperacao. ")
else:
    print(f"Aluno(a) Reprovado(a) com media {media:.2f}")