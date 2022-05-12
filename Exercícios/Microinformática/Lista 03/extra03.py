#Ler dois npumeros inteiros, mostrar na tela o maior dele e também a diferença

num1 = int(input("Digite o primero número: "))
num2 = int(input("Digite o segundo número: "))

#Maior
if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1

print(f"\nO número maior é o: {maior}")
print("A diferença entre eles é: ", maior-menor )
print("\nOs números entre eles são os: ")
#Numeros entre
while(num2 >= num1):
    print(num1)
    num1 = num1 + 1


