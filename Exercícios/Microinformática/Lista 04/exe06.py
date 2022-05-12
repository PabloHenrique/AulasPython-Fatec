#Ler n números. Calcular soma dos pares e dos ímpares

num = 0
cont = 1
somaPar = 0
somaImpar = 0

qt = int(input("Informe a quantidade de números a serem informados: "))

while(cont <= qt):
    num = int(input("Digite um número: "))
    cont+=1
    if(num%2 == 0):
        somaPar += num
    else:
        somaImpar += num

print(f"\nA soma dos números ímpares resulta em: {somaImpar}")
print(f"A soma dos números pares resulta em: {somaPar}")