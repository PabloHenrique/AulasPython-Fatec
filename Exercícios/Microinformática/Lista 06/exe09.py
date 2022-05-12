from random import randint
v = []
encontrado = False

for i in range(10):
    v.append(randint(1,50))

num = int(input("Informe um número(1 - 50): "))

for i in range(10): #or i in NomeVetor
    if v[i] == num:
        encontrado = True
        break

print(v)
if encontrado:
    print("Número encontrado")
else:
    print("Número não encontrado")