#Ler um número inteiro e inverter

num = int(input("Digite um número: "))
inv = 0
while (num > 0):
    ult = num % 10
    inv = (inv * 10) + ult
    num //= 10
print(f"O número resultou em: {inv}")