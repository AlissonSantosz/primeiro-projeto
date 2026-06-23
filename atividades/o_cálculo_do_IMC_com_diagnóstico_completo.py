peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)

if imc < 18.5:
    diagnostico = ("Abaixo do peso")
elif imc < 25:
    diagnostico = ("Peso ideal, parabéns")
elif imc < 30:
    diagnostico = ("Levemente acima do peso")
elif imc < 35:
    diagnostico = ("Obesidade Grau I")
else:
    diagnostico = ("Obesidade Severa/Mórbida")

print(f"\n Seu IMC é: {imc:.2f}")
print(f"Diagnóstico: {diagnostico}")
