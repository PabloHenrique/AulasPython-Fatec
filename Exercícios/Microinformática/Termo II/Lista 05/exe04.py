'''
Defina a função prod_lista que recebe como argumento uma lista de
números inteiros e devolve o produto dos seus elementos
'''
from random import randint
from functools import reduce

def prod_lista(L):
    return reduce(lambda x,y: x*y,L)

lista = [randint(1,10) for i in range(5)]
print('Números geraodos >>',lista)
print('Produto dos valores >>',prod_lista(lista))