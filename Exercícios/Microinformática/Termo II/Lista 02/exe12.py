'''
Faça um programa que leia um número inteiro positivo impar N e calcule o fatorial duplo
desse número. O fatorial duplo é definido como o produto de todos os números naturais ímpares de
1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é: 5!! = 1 * 3 * 5 = 15
Faça funções para validação da entrada e para o cálculo do fatorial duplo.
'''

def fatDuplo(n):
    fat = 1
    for i in range(1,n+1,2):
        fat *= i
    return fat

N = int(input('Informe o número >> '))
print(f'{N}!! = {fatDuplo(N)}')
