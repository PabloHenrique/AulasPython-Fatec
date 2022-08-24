'''
Faça um programa em Python que leia uma matriz 2 x 3 de inteiros,
imprima a matriz e a soma de todos os elementos.
'''

soma = 0
from random import randint

M = [0] * 10
for linha in range (10):
    M[linha] = [0] * 10
    for coluna in range(10):
        M[linha][coluna] = randint(1, 50)
        soma += M[linha][coluna]

print('\nResultado da Matriz: \n')
for m in range(10):
    for n in range(10):
        print(f'{M[m][n]:02}', end=' ')
    print()

media = soma // 6
print(f'\nA média resultou em: {media}')
