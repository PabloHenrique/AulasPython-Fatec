from random import randint
A = []
B = []
C = []

for i in range(20):
    A.append(randint(1,50))
    if A[i]%2 == 0:
        B.append(A[i])
    else:
        C.append(A[i])

print(A)
print("Par >>",B)
print("Ímpares >>",C)