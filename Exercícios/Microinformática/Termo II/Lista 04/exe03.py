'''
Faça um programa que gere aleatoriamente duas listas de 10 posições (valores entre 1 e 50) e calcule
outra lista contendo, nas posições pares os valores da primeira lista e nas posições ímpares os valores da
segunda lista.
'''

from random import randint
A = []
B = []
C = []

for i in range(10):
    A.append(randint(1,50))
    B.append(randint(1,50))
print('A ->',A)
print('B ->',B)

for i in range(10):
    C.append(A[i])
    C.append(B[i])
print('C ->',C)