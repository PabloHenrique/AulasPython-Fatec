'''
Defina a função media_digitos que recebe como argumento um número natural
e devolve a média dos seus dígitos.
'''
def media_digitos(num):
    '''
    #Da forma tradicional
    soma = 0
    c = 0
    while num != 0:
        soma += num%10
        num //= 10
        c += 1
    return soma/c
    '''
    digitos = list(map(int,str(num)))
    print(digitos)
    return sum(digitos)/len(digitos)

N = int(input('Informe um número >> '))
print(f'A média dos dígitos do número {N} é {media_digitos(N):.2f}')