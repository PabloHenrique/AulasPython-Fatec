from random import randint
sim = True

'''Testar vetor decrescente'''
#V = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

V = [0] * 20
for i in range(20):
    V[i] = randint(1, 30)

print("\nVetor gerado: ")
print(V)

for c in range(19):
    proximo = V[c+1]
    if(V[c] > proximo):
        sim = True
    else:
        sim = False
        break

if sim:
    print('\nDecrescente')
else:
    print('\nNão é decrescente')