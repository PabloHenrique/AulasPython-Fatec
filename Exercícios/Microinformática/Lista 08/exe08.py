'''
Elabore um programa em Python que leia duas matrizes A (mxn) e B (pxq)
e calcule e mostre a matriz Python que é a soma de A com B (caso a soma seja possível).
'''

from random import randint

#vai rolar se MXN e NXM 2x1 1x2
m = int(input("Informe a quantidade de linhas da primeira matriz >> "))
n = int(input("Informe a quantidade de colunas da primeira matriz >> "))

p = int(input("Informe a quantidade de linhas da segunda matriz >> "))
q = int(input("Informe a quantidade de colunas da segunda matriz >> "))

if m == p and n == q:
    M1 = [0] * m
    for l in range(m):
        M1[l] = [0] * n
        for c in range(n):
            M1[l][c] = randint(1, 50)

    print('\nMatriz 01: \n')
    for m in range(p):
        for n in range(q):
            print(f'{M1[p][q]:02}', end=' ')
        print()

    M2 = [0] * p
    for l in range(p):
        M2[l] = [0] * q
        for c in range(q):
            M2[l][c] = randint(0, 50)

    print('\nMatriz 02: \n')
    for m in range(p):
        for n in range(q):
            print(f'{M2[p][q]:02}', end=' ')
        print()

    M3 = [0] * p
    for l in range(p):
        M3[l] = [0] * q
        for c in range(q):
            M3[l][c] = M1[l][c] + M2[l][c]

    print('\nMatriz 03: \n')
    for m in range(p):
        for n in range(q):
            print(f'{M3[p][q]:02}', end=' ')
        print()
else:
    print("\nNão é possível realizar a soma")