'''
Defina a função quadrados que recebe como argumento um número natural
n devolve a lista dos n primeiros quadrados perfeitos.
'''

def quadrados(n):
    '''L = []
    for i in range(1,n+1):
        L.append(i**2)'''
    return [i**2 for i in range(1,n+1)]

N = int(input('Informe um valor -> '))
print(f'{N} primeiros quadrados perfeitos -> {quadrados(N)}')