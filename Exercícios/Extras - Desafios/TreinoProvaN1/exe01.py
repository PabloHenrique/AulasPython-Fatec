#Ex1 Treino para a prova

nota = float(input("Digite a sua nota: "))
while (nota < 0 or nota > 10):
    nota = float(input("Valores inválidos, digite a nota novamente: "))
if (nota < 3):
    print("Nota conceitual: E")
elif(nota < 5):
    print("Nota conceitual: D")
elif(nota < 7):
    print("Nota conceitual: C")
elif(nota < 9):
    print("Nota conceitual: B")
elif(nota <= 10):
    print("Nota conceitual: A")