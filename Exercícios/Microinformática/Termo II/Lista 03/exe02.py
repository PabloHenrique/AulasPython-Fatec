from random import randint

def busca(lista, elem):
    if lista[0] == elem:
        return True
    if len(lista) == 1:
        return False
    return busca(lista[1:], elem)

L = []
for i in range(10):
    L.append(randint(1,30))
print(L)
x = randint(1,30)
print('Elemento gerado >>',x)
if busca(L, x):
    print(f'{x} está na lista')
else:
    print(f'{x} não está na lista')