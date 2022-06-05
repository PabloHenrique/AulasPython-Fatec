'''
Elabore  um  programa  em Python que  gere  uma  matriz  4x6
e calcule  e  mostre  a  sua  matriz transposta equivalente.
'''

from random import randint

M = [0] * 4
for l in range(4):
    M[l] = [0] * 6
    for c in range(6):
        M[l][c] = randint(0, 50)

print('\nResultado da Matriz: \n')
for m in range(4):
    for n in range(6):
        print(f'{M[m][n]:02}', end=' ')
    print()

N = [0] * 6
for l in range(6):
    N[l] = [0] * 4
    for c in range(4):
        N[l][c] = M[c][l]

print('\nResultado da Matriz: \n')
for m in range(6):
    for n in range(4):
        print(f'{N[m][n]:02}', end=' ')
    print()