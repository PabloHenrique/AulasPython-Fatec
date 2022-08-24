'''
Faça um programa em Python que gere uma matriz 10 x 10 de inteiros
aleatórios entre 1 e 50, imprima a matriz e a soma de todos
os elementos de cada linha.
'''
#from termcolor import colored
somaLinhas = [0] * 10
from random import randint

M = [0] * 10
for linha in range(10):
    M[linha] = [0] * 10
    for coluna in range(10):
        M[linha][coluna] = randint(1, 50)
        somaLinhas[linha] += M[linha][coluna]


print('\nResultado da Matriz: \n')
for m in range(10):
    for n in range(10):
        print(f'{M[m][n]:02}', end=' ')
        #print(colored(f'{M[m][n]:02}',red), end=' ')
    print()

print(f'\nA soma resultou em: {somaLinhas}')