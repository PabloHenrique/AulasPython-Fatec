from random import randint

A, B, C = [], [], []

for i in range(10):
    A.append(randint(1,10))
    B.append(randint(1,10))
A.sort()
B.sort()
print('Primeiro conjunto:',*A)
print('Segundo conjunto:',*B)
i = j = 0

while len(C) != 20:
    if i < 10 and j < 10:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    elif j == 10:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1
print('Resultado:',*C)
