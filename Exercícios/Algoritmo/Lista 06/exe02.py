#Ler um número e calcular a tabuada

n = int(input("Informe um número: "))
cont = 1

while cont <= 10:
    r = n* cont
    print(f"{n} * {cont}9 = {r}")
    cont+=1
