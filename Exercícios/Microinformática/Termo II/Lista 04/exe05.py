'''Faça um programa em Python para gerar uma lista de 20 números aleatórios entre 1 e 50. Imprima a
lista. Após isto, deverá ser lido um número qualquer e verificar se esse número existe na lista ou não. Se
existir, gerar uma nova lista sem esse número (remova todas as ocorrências do número). Imprima a nova
lista.
'''

from random import randint
L = []
for i in range(20):
    L.append(randint(1,50))
print(L)
x = int(input('Informe o número para remoção -> '))
if x in L:
    M = L.copy()
    for i in range(L.count(x)):
        M.remove(x)
    print(M)
else:
    print(f'{x} não pertence a lista')