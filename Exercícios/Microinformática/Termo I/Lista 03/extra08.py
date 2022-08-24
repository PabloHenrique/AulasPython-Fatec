#Ler uma data e verificar se ela é válida
'''
Fevereiro tem 29 dias em anos bissextos
Fevereiro tem 28 dias em anos não bissextos
'''

data = input("Informe uma data[dd/mm/yyyy]: ")

dataSplit = data.split('/')
dataSplit[0] = int(dataSplit[0])
dataSplit[1] = int(dataSplit[1])
dataSplit[2] = int(dataSplit[2])

if dataSplit[1] > 0 and dataSplit[1] < 13:
    if dataSplit[2] > 0:
        if (dataSplit[1] == 2 and ((dataSplit[2] % 400 == 0) or (dataSplit[2] % 100 != 0 and dataSplit[2] % 4 == 0)) and
            (dataSplit[0] > 0 and dataSplit[0] <= 29)):
            print(f"Data {data} é válida")
        elif dataSplit[1] == 2 and (dataSplit[0] > 0 and dataSplit[0] <= 28):
            print(f"Data {data} é válida")
        elif dataSplit[1] == 4 or dataSplit[1] == 6 or dataSplit[1] == 9 or dataSplit[1] == 11:
            if dataSplit[0] > 0 and dataSplit[0] <= 30:
                print(f"Data {data} é válida")
            else:
                print("Dia inválido")
        elif dataSplit[0] > 0 and dataSplit[0] <= 31:
            print(f"Data {data} é válida")
        else:
            print("Dia inválido")
    else:
        print("Ano inválido")
else:
    print("Mês inválido")