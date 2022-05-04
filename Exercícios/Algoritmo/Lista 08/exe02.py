#Calcular fatorial
fat = 1
num = int(input("Digite um número: "))

for i in range(1, num+1):
    fat *= i
    print(fat)

print(f"O fatorial do número {num} resulta em: {fat}")