'''
Faça um programa que peça as temperaturas de uma determinada cidade em um determinado mês.
Armazene em uma matriz 4x7, onde a linha representa cada semana do mês.
Imprima a matriz e mostre a média das temperaturas do mÊs.
'''
soma = 0
from random import randint
from random import random

M = [0] * 4
for linha in range (4):
    M[linha] = [0] * 7
    for coluna in range(7):
        M[linha][coluna] = random()*50
        soma += M[linha][coluna]

print('\nResultado da Matriz: \n')
for m in range(4):
    for n in range(7):
        print(f'{M[m][n]:.0002}º', end=' ')
    print()


media = soma // 28

print(f'\nA média das temperaturas resultou em: {media}')