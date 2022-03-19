#Ler os ângulos e informar qual a sua classificação.

print("Medidas de ângulos de um triângulo >>>>>>")

a = float(input("\nInforme o ângulo do lado A: "))
b = float(input("Informe o ângulo do lado B: "))
c = float(input("Informe o ângulo do lado C: "))

if a+b+c == 180 and a != 0 and b != 0 and c != 0:
    if a == 90 or b == 90 or c == 90:
        print("\nTriângulo retângulo")

    elif a > 90 or b > 90 or c > 90:
        print("\nTriângulo obtusângulo")

    elif a < 90 and b < 90 and c < 90:
        print("\nTriângulo acutângulo")
else:
    print("\nTriângulo inválido!")