retaA = float(input("Digite a retaA: "))
retaB = float(input("Digite a retaB: "))
retaC = float(input("Digite a retaC: "))

if retaA + retaB < retaC or retaA + retaC < retaB or retaB + retaC < retaA:
    print("Os lados informados não podem formar um triângulo.")
else:
    if retaA == retaB and retaB == retaC:
        print("Triângulo Equilátero")
    elif retaA != retaB and retaB != retaC and retaA != retaC:
        print("Triângulo Escaleno")
    else:
        print("Triângulo Isósceles")
