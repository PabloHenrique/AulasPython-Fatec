soma = 0
ult = 1

num = int(input("Digite um número de vezes: "))

for i in range(1, num+1):
    soma += i
    for c in range(ult, soma + 1):
        if c==soma:
            ult = c+1
        print(f'{c}', end=' ')
    print()

