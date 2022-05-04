#Ler as medidas de um terreno e calcular a área e o perímetro dele.

larg = float(input("Informe a largura do terreno: "))
comp = float(input("Informe o comprimento do terreno: "))

area = larg * comp
perimetro = 2 * (larg + comp)

print(f"A área do terreno é {area} e o perímetro do terreno é {perimetro}")