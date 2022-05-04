#Ex2 Treino para a prova

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo: "))
soma = 0

if(n2 < n1):
    print("Valores inválidos!")
else:
    while(n2 >= n1):
        soma += n2
        n2 -= 1
    print(f"O valor das somas é: {soma}")