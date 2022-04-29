#Poluição Aula 09 - 02

ip = float(input("Digite o índice de poluição: "))

if(ip <= 0.25):
    print("Índice de polução OK!")
elif(ip < 0.3):
    print("Industrias do Grupo 1 - Atividades Suspensas!")
elif(ip < 0.4):
    print("Industrias do Grupo 1 e 2 - Atividades Suspensas!")
else:
    print("Todas as industrias - Atividades Suspensas!")