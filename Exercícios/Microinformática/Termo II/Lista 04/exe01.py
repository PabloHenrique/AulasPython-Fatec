'''
Faça um programa que gere uma lista de 20 números aleatórios entre 1 e 10.
Leia um número x entre 1 e 10. Imprima a lista e mostre quantos números
iguais a x tem na lista.
'''
from random import randint

L = []
for i in range(20):
    L.append(randint(1,10))
print(L)
x = int(input('Informe um números de 1 a 10 -> '))
ocorrencias = L.count(x)
print(f'Tem {ocorrencias} vezes o número {x} na lista')