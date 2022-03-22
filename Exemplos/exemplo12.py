#Exemplo - While - Validar determinado valor
#Entrar com uma nota de 0 à 10

nota = -1
while(nota < 0 or nota > 10):
    nota = int(input("\nDigite uma nota: "))
    if (0 <= nota <= 10):
        print(f"\nNota informada: {nota}")
        print("FIM")
    else:
        print("\nNota inválida!")
