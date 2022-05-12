from random import randint
v = []
indice = 0
igual = True

v.append(randint(1, 50))

while len(v) != 10:
    x = randint(1, 50)
    for i in range(len(v)):
        if v[i] == x:
            igual = False
    if igual:
        v.append(x)
    igual = True
print(v)