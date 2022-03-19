#Ler altura, peso e sexo de uma pessoa. Informar o peso ideal.

altura = float(input("Digite sua altura: "))
sexo = input("Digite o sexo [F/M]:").upper()[0] #Função para capturar a primeira posição + deixar em caixa alta
if (sexo == 'F' or sexo == 'M'):
    if(sexo == 'F'):
        pesoIdeal = 62.1 * altura - 44.7
    else:
        pesoIdeal = 72.7 * altura - 58
    print(f"O peso ideal resulta em {pesoIdeal:.2f}Kg")
else:
    print("Entrada de dados inválida. Tente com [F/M]")