from random import randint
v = []
menor = 0
indice = 0

for i in range(10):
    v.append(randint(1,50))
print("Antes >>",v)

#Selection Sort
for j in range(10):
    for i in range(indice,10):
        if v[menor] > v[i]:
            menor = i
        if i == 9:
            v[indice],v[menor] = v[menor],v[indice]
            indice += 1
            menor = indice
print("Depois >>",v)

'''
v.sort()
'''