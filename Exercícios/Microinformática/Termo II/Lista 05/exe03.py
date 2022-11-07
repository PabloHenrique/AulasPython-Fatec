'''
Defina a função indices_pares que recebe como argumento uma lista de números
inteiros w e devolve a lista dos elementos de w em posições pares.
'''
from random import randint

def indices_pares(w):
    #return [w[i] for i in range(0,len(w),2)]
    #return [w[i] for i in range(len(w)) if i % 2 == 0]
    return [num for num in w[::2]]
    #return [num for i,num in enumerate(w) if i % 2 == 0]


lista = [randint(1,50) for i in range(10)]
print('Números geraodos >>',lista)
print('Número das posições pares >>',indices_pares(lista))