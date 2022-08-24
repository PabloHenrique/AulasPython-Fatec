soma1 = 0
soma2 = 0

n1 = int(input("Informe um número: "))
n2 = int(input("Informe o segundo número: "))

for c in range(1, (n1//2)+1):
    if (n1%c == 0):
        soma1 += c

for d in range(1, (n2//2)+1):
    if (n2%d == 0):
        soma2 += d

if (soma1 == n2 and soma2 == n1):
    print(f"\nOs números {n1} e {n2} são amigos!")

else:
    print(f"\nOs números não são amigos!")

