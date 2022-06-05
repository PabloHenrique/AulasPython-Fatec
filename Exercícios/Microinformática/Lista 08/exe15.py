'''
Elabore um programa em Python que gere uma matriz aleatória (9x9), com números entre 0 e
10, imprima-a. Após, peça o quadrante desejado e imprima os elementos desse quadrante.
'''

from random import randint

M = [0] * 9
for l in range(9):
    M[l] = [0] * 9
    for c in range(9):
        M[l][c] = randint(0,10)

for i in range(9):
    for j in range(9):
        print(f"{M[i][j]:02} ",end=' ')
    print()

print("\nResultado!")
for i in range(9):
    for j in range(9):
        if(M[4][j] or M[i][4]):
            M[4][j] = "X "
            M[i][4] = "X "

for i in range(9):
    for j in range(9):
        print(f"{M[i][j]:02} ",end=' ')
    print()