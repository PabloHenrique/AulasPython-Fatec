#Ler um número inteiro, verificar se ele é perfeito.

num = int(input("Digite um número: "))
sd = 0

for i in range(1, num//2+1):
    if(num%i == 0):
        sd += i

if(sd == num):
    print("O número é perfeito!")

else:
    print("O número NÃO é perfeito!")
    