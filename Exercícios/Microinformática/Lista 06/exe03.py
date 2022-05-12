from random import randint
v = []
m = []
for i in range(20):
    v.append(randint(1,50))
    if v[i]%5 == 0:
        m.append(v[i])

print("lista completa >> ",*v)
print("lista de multiplos >> ",*m)