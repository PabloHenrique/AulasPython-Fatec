#Calcular a média das idades de um grupo de pessoas

cont = 0
media = 0
soma = 0
while True:
    idade = int(input("Digite a sua idade: "))
    cont += 1
    if(idade == 0):
        break
    else:
        soma += idade
        media = soma / cont
print(f"Foram obtidas {cont} idades! A média resultou em: {media}")