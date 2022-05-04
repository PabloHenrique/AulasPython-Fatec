#Ex3 Treino para a prova

n = int(input("Digite o total de termos: "))
cont = 1

if(n <= 0):
    print("Valores inválidos")
else:
    while(n >= cont):
        res = cont ** 2
        print(f"\n{cont}² = {res}")
        cont += 1