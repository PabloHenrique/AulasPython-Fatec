from random import randint
v = []
n = int(input("Informe um número: "))
for i in range(20):
    v.append(randint(1,50))
    if v[i]%n == 0:
        print(v[i])
print("lista >> ",v)