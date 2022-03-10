#Leia um número de 3 algarismos menores de 1000 e informe se ele é ascendente

n = int(input("Informe um número: "))

if n >= 1000:
    print("Número inválido")
else:
    n1 = n//100
    n2 = (n%100)//10
    n3 = n%10

    if n2 > n1 and n2 < n3:
        print("Ascendente!")
    else:
        print("Não ascendente!")
