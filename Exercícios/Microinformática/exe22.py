#Gerar um conjunto de 20 números inteiros aleatórios entre 1 e 50. Mostrar o maior e o menor valor.

import random
cont = 1
maior = 0
menor = 52

while(cont <= 20):
    num = random.randint(1,52)
    print(num)
    if(num > maior):
        maior = num
    if(num < menor):
        menor = num
    cont += 1

print(f"\nO número maior é o {maior}")
print(f"\nE o menor é o {menor}")