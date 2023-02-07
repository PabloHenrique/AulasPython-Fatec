'''
Fatec Garça - ADS - Termo 1 - Noite
Caue Vicentini Ruiz
Pablo Henrique Nadai

Avaliação - 04
Caça Números.

2022 05 19
'''
tem = False
import random

L = list()

for i in range(20):
    L.append(random.randint(0,9))
print(L)

n = int(input('Digite um número de 100 à 999: '))
while True:
    if 99<n<=999:
       break
    else:
        n = int(input('Erro: Digite um número de 100 à 999: '))

for j in range(18):
    if n == (L[j]*100 + L[j+1]*10 + L[j+2]):
        print(f'{j} {j+1} {j+2}')
        tem = True
        break
    elif n == (L[j+2]*100 + L[j+1]*10 + L[j]):
        print(f'{j+2} {j+1} {j}')
        tem = True
        break

if (tem == False):
    print('Não existe')

