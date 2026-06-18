from xml.dom.minidom import ProcessingInstruction

salario = float(input("Digite seu salario bruto"))
parcela = float(input("Valor da parcela"))

if parcela <= salario * 0.3:
 print("Credito aprovado")

else:
    print("Credito reprovado")