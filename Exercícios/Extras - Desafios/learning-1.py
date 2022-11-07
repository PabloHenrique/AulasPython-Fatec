#Calcular a distância entre dois pontos
import math

print("Digite as coordenadas: ")
xa = int(input("XA >> "))
ya = int(input("YA >> "))
xb = int(input("XB >> "))
yb = int(input("YB >> "))

res = 0

print("\n\nResponda conforme a tabela abaixo.")
print("Digite 1. Se um dos eixos forem iguais.")
print("Digite 2. Fórmula geral.")
situacao = int(input(">> "))

lado1 = xb - xa
lado2 = yb - ya
while True:
    if(situacao == 1):
        if(ya == yb):
            res = xb - xa
        elif(xa == ya):
            res = yb - ya
        break
    elif(situacao == 2):
        res = math.sqrt((lado1 ** 2)+(lado2 ** 2))
        break
    else:
        print("Situação inválida.\nTente novamente!")
        situacao = int(input("Digite >> "))

print("\n\nAs coordenadas são: ")
print(F"Ponto 1 - ({xa},{ya})")
print(F"Ponto 2 - ({xb},{yb})")

print("A distância entre os dois pontos é: ",res)