from random import randint
v = [0]*10
par = 0
impar = 0

for i in range(10):
    v[i] = randint(1,50)
    print(v[i])
    if v[i]%2 == 0:
        par += 1
    else:
        impar += 1

print(f"Pares >> {par} - Ímpares >> {impar}")
print(v)