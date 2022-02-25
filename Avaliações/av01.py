x1 = float(input("Digite o valor do ponto X1: "))
y1 = float(input("Digite o valor do ponto Y1: "))

x2 = float(input("Digite o valor do ponto X2: "))
y2 = float(input("Digite o valor do ponto Y2: "))

distancia = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
raiz = distancia ** 0.5

print(f"{raiz:.4f}")