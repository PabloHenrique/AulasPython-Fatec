<<<<<<< HEAD
#calculo de área de triângulo ou retângulo, verificação de operação

print("Operações >>>>>")
print("\nÁrea do retângulo - 1")
print("Área do triângulo - 2")
op = int(input("\nInforme a operação: "))

if op != 1 and op != 2:
    print("Operação inválida!")
else:
    base = float(input("\nInforme a base da figura: "))
    altura = float(input("Informe a altura da figura: "))

    areaRetangulo = base * altura

    if op == 1:
        print("\nA área do retângulo é: ",areaRetangulo)
    else:
        areaTriangulo = areaRetangulo/2

=======
#calculo de área de triângulo ou retângulo, verificação de operação

print("Operações >>>>>")
print("\nÁrea do retângulo - 1")
print("Área do triângulo - 2")
op = int(input("\nInforme a operação: "))

if op != 1 and op != 2:
    print("Operação inválida!")
else:
    base = float(input("\nInforme a base da figura: "))
    altura = float(input("Informe a altura da figura: "))

    areaRetangulo = base * altura

    if op == 1:
        print("\nA área do retângulo é: ",areaRetangulo)
    else:
        areaTriangulo = areaRetangulo/2

>>>>>>> 2e059de1adf9b45359961e6591dfb9f4ff8fc2fb
        print("\nA área do triângulo é: ",areaTriangulo)