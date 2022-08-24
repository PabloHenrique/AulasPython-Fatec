#Ler um número, exibir o número ao quadrado e a raiz dele

num = 0
cont = 0

while (cont < 1):
    num = int(input("Digite um número: "))
    if num > 0:
        #positivo
        cont = cont + 1

        #quad
        quad = num ** 2

        #raiz
        raiz = num ** 0.5

        print(f"O número digitado ao quadrado: {quad}")
        print(f"\nE a sua raiz: {raiz}")
    else:
        print("\nEntrada inválida")
