#Ler a placa de um carro e infomar o dia da semana (rodízio)
placa = input("Informe os últimos 4 dígitos da placa de seu carro: ")

if len(placa) == 4:
    placa = int(placa)
    finalPlaca = placa % 10

    if finalPlaca == 1 or finalPlaca == 2:
        print("Dia do rodízio: Segunda-Feira")

    elif finalPlaca == 3 or finalPlaca == 4:
        print("Dia do rodízio: Terça-Feira")

    elif finalPlaca == 5 or finalPlaca == 6:
        print("Dia do rodízio: Quarta-Feira")

    elif finalPlaca == 7 or finalPlaca == 8:
        print("Dia do rodízio: Quinta-Feira")
    else:
        print("Dia do rodízio: Sexta-Feira")

    '''    
    if placa[3] == '1' or placa[3] == '2':
        print("Dia do rodízio: Segunda-Feira")
    
    elif placa[3] == '3' or placa[3] == '4':
        print("Dia do rodízio: Terça-Feira")
    
    elif placa[3] == '5' or placa[3] == '6':
        print("Dia do rodízio: Quarta-Feira")
    
    elif placa[3] == '7' or placa[3] == '8':
        print("Dia do rodízio: Quinta-Feira")
    
    else:
        print("Dia do rodízio: Sexta-Feira")
    '''
else:
    print("Digite valores válidos!")
