from random import randint

v = []

for i in range(10):
    v.append(randint(1,50))

print(v)
n = int(input("Escolha uma opção: "))
if n == 1:
    for i in v:
        print(i)
else:
    for i in reversed(v):
        print(i)