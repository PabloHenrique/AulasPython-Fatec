'''
Defina a função soma_nat que recebe como argumento um número natural n
e devolve a soma de todos os números naturais até n.
'''
from functools import reduce
from operator import add

def soma_nat(n):
    #return sum([i for i in range(1,n+1)])
    #return sum(range(1,n+1))
    return reduce(add, range(1,n+1))

N = int(input('Informe um valor -> '))
print(f'A soma de 1 a {N} é {soma_nat(N)}')