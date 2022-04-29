#Ler uma nota (0 - 10), caso inválida repetir entrada

while True:
    nota = int(input("Nota >> "))
    if nota >= 0 and nota <= 10:
        break
    else:
        print("Nota inválida!\n")
print("\nPrograma encerrado")
print(f"Nota = {nota}")