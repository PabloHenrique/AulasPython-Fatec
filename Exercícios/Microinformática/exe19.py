#Ler 2 notas de 10 alunos e mostre a média de cada um

cont = 1
while cont <= 10:
    print("=" * 20)
    print(f"Aluno {cont}")
    n1 = float(input("Informe a nota 1: "))
    n2 = float(input("Informe a nota 2: "))
    media = (n1+n2)/2

    print(f"A media do aluno {cont} é {media}\n")
    cont+=1