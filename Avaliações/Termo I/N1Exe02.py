#Elevar o número ao quadrado somando ímpares
somaImpar = 0
c = 0
i = 1
somaImpar = 0

print("-" * 40)
n = int(input("Digite um número: "))

while(n <= 0):
    print("-" * 20)
    print("\nNúmero inválido.")
    n = int(input("\n\nDigite novamente um número inteiro positivo: "))

#Gerar num par
while(c < n):
    # Realizar a soma dos números
    somaImpar = somaImpar + i
    #Guardar números ímpares
    i = i + 2
    #Contador
    c += 1

print("=" * 40)
print(f"\nA soma dos {n} primeiros ímpares, resulta em: {somaImpar}.")
print(f"Logo, o número {n} elevado ao quadrado também resulta em {somaImpar}!")
