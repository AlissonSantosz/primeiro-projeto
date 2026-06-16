nome = input("Digite seu nome: ")
.nome_amigo = input("Digite o nome do seu melhor amigo: ")


print(f"Olá {nome} seja bem vindo ao meu programa!")

ano_nasc = int( input(f"Prazer em te conhecer, {nome}!, \n digite o ano do seu nascimento: "))
idade = 2026 - ano_nasc
print(f"Parabéns por seus {idade} anos")

print(f"O seu melhor amigo é o {nome_amigo}")