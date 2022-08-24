'''
Faça um programa em Python que gere uma matriz 10 x 10 de inteiros
entre 1 e 50, imprima a matriz e o menor elemento de cada linha.
'''

from random import randint
L = [0] * 10
menor = [0] * 10

for l in range(10):
    L[l] = [0] * 10
    for c in range(10):
        L[l][c] = randint(1, 50)

for c in range(10):
    for l in range(10):
        if c == 0:
            menor[l] = L[l][c]
        elif L[l][c] < menor[c]:
            menor[l] = L[l][c]

print('\nResultado da Matriz: \n')
for m in range(10):
    for n in range(10):
        print(f'{L[m][n]:02}', end=' ')
    print()
print(menor)
