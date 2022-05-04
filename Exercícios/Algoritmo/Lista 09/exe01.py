#João o Pescador Aula 09 - 01
cont = 1
multa = 0
fim = 0
while True:
    print("-" * 30)
    print(f"Peixe número {cont}!")
    print("-" * 30)
    cont += 1
    p = float(input("Digite o peso do peixe: "))
    if(p > 50):
        multa += 4
        print(f"O peso do peixe {cont} é maior do que R$50!")
        print(f"\nVocê levou uma multa!")
    fim = int(input("\n\nDeseja continuar? (0 == SIM)\n"))
    if(fim != 0):
        print("Analisando os resultados!")
        print(f"Total de peixes: {cont-1}")
        print(f"Total de multas: R${multa}")
        break