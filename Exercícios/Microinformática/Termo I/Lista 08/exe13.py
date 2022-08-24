'''
Escreva um programa em Python que gere uma matriz M[5][5], com números aleatórios entre
1 e 50. Imprima a matriz. A seguir, troque os elementos da diagonal principal com os elementos
da diagonal secundária. Imprima a nova matriz.
'''

from random import randint

M = [0] * 5
for l in range(5):
    M[l] = [0] * 10
    for c in range(5):
        M[l][c] = randint(0, 50)
'''
Diagonal principal [i == j]
Diagonal secundária [i + j = 4]
'''
for i in range(5):
    for j in range(5):
        print(f"{M[i][j]:02} ", end=' ')
    print()

print("\nResultado!")
for i in range(5):
    M[i][i], M[i][4-i] = M[i][4-i], M[i][i]

for i in range(5):
    for j in range(5):
        print(f"{M[i][j]:02} ", end=' ')
    print()