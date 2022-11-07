'''
Gere uma lista 20 números aleatórios entre 1 e 50 e mostre qual o maior valor da lista,
o menor e a média dos valores
'''

from random import randint

L = []
for i in range(20):
    L.append(randint(1,50))
print(L)
print('Maior ->',max(L))
print('Menor ->',min(L))
print('Média ->',sum(L)/len(L))