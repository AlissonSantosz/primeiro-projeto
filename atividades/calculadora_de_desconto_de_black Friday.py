valor_compra = float(input("Digite o valor total da compra: R$ "))

if valor_compra <= 100:
    desconto = 0
    print(f"Sua compra foi de R$`{valor_compra} e você não teve desconto")
elif valor_compra <= 300:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f"Sua compra foi de R$ `{valor_compra} pois voce teve um desconto de R$ {desconto} e o seu pagamento  final será de {valor_final}")
elif valor_compra <= 500:
    desconto = valor_compra * 0.1
    valor_final = valor_compra - desconto
    print(f"Sua compra foi de R$ {valor_compra} pois você teve um desconto de R${desconto} e o seu pagamento final vai ser de R${valor_final}")

else:
    desconto = valor_compra * 0.15
    valor_final = valor_compra - desconto
    print(f"Sua compra foi de R${valor_compra} pois você teve um desconto de R${desconto} e o seu pagamento final vai ser de R${valor_final}")
