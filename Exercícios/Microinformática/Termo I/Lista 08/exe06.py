'''
Elabore um programa em Python que gere uma matriz 5x5
e calcule e mostre a diagonal principal e a secundária.
'''

from random import randint
M = [0] * 5
for l in range(5):
    M[l] = [0] * 5
    for c in range(5):
        M[l][c] = randint(1, 50)


print('\nResultado da Matriz: \n')
for m in range(5):
    for n in range(5):
        print(f'{M[m][n]:02}', end=' ')
    print()

print('\nResultado da Diagonal Primária: \n')
for m in range(5):
    for n in range(5):
        if m == n:
            print(f'{M[m][n]:02}', end=' ')
        else:
            print('x', end=' ')
    print()

print('\nResultado da Diagonal Secundário: \n')
for m in range(5):
    for n in range(5):
        if m + n == 4:
            print(f'{M[m][n]:02}', end=' ')
        else:
            print('x', end=' ')
    print()



