import random
v = [0] * 20
soma, par = 0, 0

for i in range(20):
    v[i] = random.randint(1,50)
    if v[i]%2 == 0:
        print(v[i])
        soma += v[i]
        par += 1
media = soma/par
print("media de pares >> ",media)