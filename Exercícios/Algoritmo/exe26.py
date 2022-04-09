#Ler um número inteiro e determinar a quantidade de algarismo

qt_algarismo = 0
n = int(input("Informe um número: "))

while n > 0:
    n //= 10
    qt_algarismo += 1
print(f"{qt_algarismo} algorismo(s)")
