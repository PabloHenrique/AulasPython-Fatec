#Ler um número inteiro e exibir os seus algarismos separadamente.

n = int(input("Informe um número inteiro: "))

centena = n//100
dezena = (n%100)//10
unidade = n%10

print(f"{centena} centenas, {dezena} dezenas e {unidade} unidades")