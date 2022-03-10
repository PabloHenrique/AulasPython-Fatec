#Ler as medidas de um triângulo e informar qual a sua classificação.

print("Medidas de um triângulo >>>>>>")

a = float(input("\nInforme a medida do lado A: "))
b = float(input("Informe a medida do lado B: "))
c = float(input("Informe a medida do lado C: "))

#Validação
if a < b + c and b < a + c and c < a + b:
    if (a == b and a == c):
        print("\nEquilátero")
    elif(a == b or a == c or b == c):
        print("\nIsóceles")
    else:
        print("\nEscaleno")
else:
    print("Medidas inválidas!")