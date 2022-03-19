#Ler um número com 1 à 3 algarismos.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

v = 0
somaDezena = 0
somaCentena = 0

c1 = num1 // 100
d1 = (num1 % 100) // 10
u1 = num1 % 10

c2 = num2 // 100
d2 = (num2 % 100) // 10
u2 = num2 % 10

somaUnidade = u1 + u2
if somaUnidade > 9:
    v += 1
    somaDezena += 1

somaDezena = d1 + d2
if somaDezena > 9:
    v += 1
    somaCentena += 1

somaCentena = c1 + c2
if somaCentena > 9:
    v += 1

print(v, "vai 1")
