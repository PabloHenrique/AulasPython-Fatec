from random import randint

A, B, C = [], [], []

while len(A) != 10:
    num = randint(1,20)
    if num not in A:
        A.append(num)
print('Primeiro conjunto:',A)

while len(B) != 10:
    num = randint(1,20)
    if num not in B:
        B.append(num)
print('Segundo conjunto:',B)

for i in range(10):
    if A[i] in B:
        C.append(A[i])
print('Resultado(A-B):',C)