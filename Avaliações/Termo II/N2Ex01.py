'''
Faça um programa em Python que gere uma lista com 20 números aleatórios
entre 1 e 50 e imprima a  lista  ordenada  da  seguinte  forma:  todos
os  pares  em  ordem  crescente  e em  seguida todos  os ímpares em ordem
decrescente.Mantendo o resultado na mesma lista.
'''
import time
from random import randint

L = []
for i in range(20):
    L.append(randint(1, 50))

print("\n\nOláa! Segue a lista gerada: ")
print(L)

time.sleep(1)
print("\n\nIniciando ordenação...")
time.sleep(2)

PAR = []
IMPAR = []

for i in range(20):
    if L[i] % 2 == 0:
        PAR.append(L[i])
    else:
        IMPAR.append(L[i])

PAR.sort()
IMPAR.sort(reverse=True)

L.clear()

for j in range(len(PAR)):
    L.append(PAR[j])

for k in range(len(IMPAR)):
    L.append(IMPAR[k])

print("-"*50)
print("\nSegue resultados: ")
print(L)
print("-"*50)

print("\nTotal de números pares encontrados: ")
print(F"Quantidade: {len(PAR)} Valores: {PAR}")
print("\nTotal de números ímpares encontrados: ")
print(F"Quantidade: {len(IMPAR)} Valores: {IMPAR}")