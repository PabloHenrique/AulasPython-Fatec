#Verificar se um número é primo


cont = 0
i = 0


while True:
    num = int(input("\n\nDigite um número: "))
    if(num == 0):
        break
    if(num > 1):
        while (i <= num or cont < 2):
            i = i + 1
            x = num % i
            if (x == 0):
                cont = cont + 1
        if cont <= 2:
            print(f"O número {num} É PRIMO!")
        else:
            print(f"O número {num} NÃO é primo.")
    else:
        print(f"O número {num} NÃO é primo.")