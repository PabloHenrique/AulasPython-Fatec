idade = int(input("Digite sua idade:"))

if idade < 0:
    print("Digite uma idade válida!")
else:
    if idade <= 10:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade >= 18:
        print("Adulto")
