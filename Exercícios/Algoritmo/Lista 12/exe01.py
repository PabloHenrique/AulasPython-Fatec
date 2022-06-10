from random import randint

M = [0] * 5
for l in range(5):
    M[l] = [0] * 5
    for c in range(5):
        M[l][c] = randint(0, 10)

print("\nCompleta")
for i in range(5):
    for j in range(5):
        print(f'{M[i][j]:2}', end=' ')
    print()

print("\nPrincipal")
for i in range(5):
    for j in range(5):
        if i == j:
            print(M[i][j])

print("\nSecundária")

for i in range(5):
    for j in range(5):
        if i + j == 4:
            print(M[i][j])
