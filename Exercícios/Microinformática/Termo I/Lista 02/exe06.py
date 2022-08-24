#Ler três números, colocar em ordem crescente.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if b == a:
    input("O primeiro número é idêntico ao segundo. Erro!")
else:
    c = int(input("Digite o terceiro número: "))
    if c != b and a != c:
        if b > a and b > c:
            b, c = c, b

        elif a > c:
            c, a = a, c

        if a > b:
            b, a = a, b

        print(f"\nA ordem é: Valores: {a} < {b} < {c}")
    else:
        input("Números idênticos. Erro!")




