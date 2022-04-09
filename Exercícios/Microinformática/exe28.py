#Verificar se um número é primo ou não.

num = int(input("Digite um número: "))

if(num <= 1):
    print("Não é primo")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print("Não é primo")
            break
    else:
        print("É primo")