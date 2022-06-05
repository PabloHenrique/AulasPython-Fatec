'''
Faça um programa em Python que gere uma matriz M[10][10] com números aleatórios de 1 a
50 e copie para um vetor de 10 elementos, os números da diagonal principal. Imprima a matriz
e o vetor.
'''
from random import randint

M = [0] * 10
val = [0] * 10

for l in range(10):
    M[l] = [0] * 10
    for c in range(10):
        M[l][c] = randint(0, 50)

for i in range(10):
    for j in range(10):
        if(i == j):
            val[i] = M[i][j]
        print(f"{M[i][j]:02} ", end=' ')
    print()

print("\n\nVetor da diagonal principal!")
print(val)