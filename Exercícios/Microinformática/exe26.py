#Ler um número inteiro de 4 algarismo. Verificar se (MC + DU)** 2 é igual ao número.

num = int(input("Digite um número: "))

while True:
    if(num < 1000 and num < 9999):
        print("\nO número deve estar entre 999 à 9999!")
        num = int(input("Digite novamente: "))
    else:
        break

unidade = num % 10
dezena = (num // 10) % 10
centena = (num //100) % 10
milhar = (num // 1000)

valor1 = dezena * 10 + unidade
valor2 = milhar * 10 + centena

soma = valor1 + valor2
quad = soma ** 2

if(quad == num):
    print("O número atende a propriedade!")
    print(f"{soma}² = {num}")
else:
    print("O número NÃO atende a propriedade!")
    print(f"{valor1} + {valor2} = {soma}")
    print(f"{soma}² não é igual à {num}")