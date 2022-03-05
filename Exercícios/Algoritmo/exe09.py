#Ler dois valores inteiros positivos. Troque os números de variáveis.

a = int(input("Digite um valor para ser armazenado em 'A':"))
b = int(input("Digite um valor para ser armazenado em 'B':"))

a, b = b ,a

print(f"O valor de A, agora é {a}")
print(f"O valor de B, agora é {b}")