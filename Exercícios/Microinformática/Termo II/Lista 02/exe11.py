'''
11.	Faça uma função que receba um número N e retorne a soma dos
algarismos de N!. Ex: se N = 4, N! = 24. Logo, a soma de seus
algarismos é 6 (2 + 4).
Faça função para o cálculo do fatorial e para a soma dos dígitos.
'''

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

def somaDigitos(n):
    soma = 0
    while n != 0:
        soma += n % 10
        n //= 10
    return soma

N = int(input('Informe um número >> '))
print(f'{N}! = {fatorial(N)} - Soma dos dígitos = {somaDigitos(fatorial(N))}')

