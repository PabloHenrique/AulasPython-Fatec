#Elaborar um algoritmo que leia o peso e a altura. Calcular o IMC

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)
print(f"Seu IMC resultou em: {imc:,.2f}")
print("\nSegue a classificação: ")
print("-" * 20)
if (imc < 18.5):
    print("Peso baixo.")
else:
    if(imc <= 24.9):
        print("Peso normal.")
    else:
        if(imc <= 29.9):
            print("Sobrepeso.")
        else:
            if(imc <= 34.4):
                print("Obesidade Grau 1.")
            else:
                if (imc <= 39.9):
                    print("Obesidade Grau 2.")
                else:
                    print("Obesidade Mórbida!")
