from random import randint
A = []
B = []

for i in range(10):
    A.append(randint(1,50))

x = int(input("Informe um número: "))
for i in range(10):
    B.append(A[i]*x)

print("="*50)
print(A)
print(B)