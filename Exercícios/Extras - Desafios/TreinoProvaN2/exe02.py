'''
2.	Faça um programa em Python que gere 2 números aleatoriamente
entre 0 e 50 e armazene em um vetor todos os números entre os
dois números gerados. Imprima o vetor.
Exemplo: Números sorteados 	 a=5  e b =21
Vetor 	 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
Obs.: Faça a troca dos valores, caso o segundo número sorteado
seja menor que o primeiro.
'''

from random import randint

n1 = int(randint(0, 50))
n2 = int(randint(0, 50))

if n2 < n1:
    n1, n2 = n2, n1

v = []

print(f"Valor 1: {n1}")
print(f"Valor 2: {n2}")

for i in range(n1, n2+1):
    v.append(i)

print({*v})