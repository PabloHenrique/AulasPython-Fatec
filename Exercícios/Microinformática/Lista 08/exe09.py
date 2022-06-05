'''
Elabore um programa em Python que declare uma matriz quadrada de 10 linhas por 10 colunas
e verifique se a matriz é simétrica em relação à diagonal principal. A matriz simétrica é aquela
em que todos os elementos A( i , j) = A( j , i) para quaisquer valores de i e j. Assim, A[2,1] deverá
ser igual a A[1,2], e A[3,5] deverá ser igual a A[5,3] e assim por diante. Imprimir mensagem
“Matriz Simétrica” ou “Matriz não Simétrica”.
'''
sim = True
from random import randint

V = [0] * 10
for l in range(10):
    V[l] = [0] * 10
    for c in range(10):
        V[l][c] = randint(0,10)
for i in range(10):
    for j in range(10):
        if V[i][j] != V[j][i]:
            sim = False
        print(f"{V[i][j]:02} ", end=' ')
    print()

if sim:
    print("\nMatriz Simétrica")
else:
    print("\nMatriz NÃO Simétrica")