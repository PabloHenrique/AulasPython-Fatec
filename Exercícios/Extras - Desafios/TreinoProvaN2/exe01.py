'''
1.	Escreva um programa em Python que leia as notas das 3 avaliações
(N1, N2 e N3). Caso o aluno não tenha feito a N3 deve ser fornecido
um valor negativo. Calcular a média do semestre considerando que a
N3 substitui a nota mais baixa entre a N1 e a N2. Escrever a média
e uma mensagem que indique se o
aluno foi aprovado, ou reprovado. Média para aprovação é 6.
'''
n1 = float(input("Informe a nota da N1: "))
n2 = float(input("Informe a nota da N2: "))
aprovado = False
media = (n1 + n2)/2

if(media > 6):
    print(f"Notas: [{n1}],[{n2}]")
    print(f"Resultado da média: {media:.2f}")
    aprovado = True
else:
    print("="*30)
    print("Será necessário a N3!")
    aprovado = False
    n3 = float(input("\nInforme a nota da N3: "))
    print(f"\nNotas: [{n1}],[{n2}],[{n3}]")
    if(n1 < n2):
        print(f"\n**Para compensar, a sua nota {n1} foi substituída!")
        n1 = n3
    elif(n2 < n1):
        print(f"\n**Para compensar, a sua nota {n2} foi substituída!")
        n2 = n3
    else:
        print("Suas notas não atingiram a média!")
        aprovado = False
    media = (n1 + n2) / 2
    print(f"\nNotas: [{n1}],[{n2}]")
    print(f"Resultado da média: {media:.2f}")
    if(media > 6):
        aprovado = True

if aprovado:
    print(f"\nVocê foi aprovado! 😊")
else:
    print(f"\nVocê foi reprovado! 😢")

