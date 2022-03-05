import math

print("Valores do primeiro ponto...")
x1 = float(input("Digite X1: "))
y1 = float(input("Digite Y1: "))

print("Valores do segundo ponto...")
x2 = float(input("Digite X2: "))
y2 = float(input("Digite Y2: "))

dist = math.sqrt((x2-x1) ** 2 + (y2-y1)**2)
#dist = pow((x2-x1) ** 2 + (y2-y1)**2), (0.5)
#dist = ((x2-x1) ** 2 + (y2-y1)**2)) ** 0.5

print(f"A distância entre os dois pontos resultam em: {dist:.4f}")