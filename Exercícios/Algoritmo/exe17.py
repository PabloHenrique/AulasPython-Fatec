#Ler idade e verificar a condição de voto

idade = int(input("Digite a sua idade: "))
if idade < 16:
    print("Você não pode votar!")
else:
    if (idade < 18 or idade >= 65):
        print("Voto opcional!")
    else:
        print("Voto obrigatório!")