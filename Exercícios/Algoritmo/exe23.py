#Estrutura While
#Ler um número e exibir a soma dos anteriores

num = int(input("Digite um número: "))
contador = 1
soma = 0

while(num >= contador):
    soma += contador
    contador += 1

print(f"A soma dos números antecessores de {num}, resultam em: {soma}")
