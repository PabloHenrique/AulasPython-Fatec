#Ler as variaveis da equação de 2º grau e calcular
import math

a = float(input("Informe o valor de a >> "))
if(a == 0):
    print("Não é equação de segundo grau.")

b = float(input("Informe o valor de b >> "))
c = float(input("Informe o valor de c >> "))

delta = (b**2) - (4 * a * c)

if delta < 0:
    print("Não existe raiz")
elif delta == 0:
    print("Raiz única")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"As raízes possíveis são x1 = {x1} e x2 = {x2}")
