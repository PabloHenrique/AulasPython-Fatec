#Ler duas notas, calcular a média e verificar a aprovação.
#Classe com 60 alunos.

aluno = 60
aprovado = 0
reprovado = 0
somaMedia = 0
c = 1
d = 0

while(aluno >= c):
    print("-" * 30)
    print(f"Aluno 0{c}!")
    nota1 = float(input("\nDigite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    media = (nota1 + nota2) /2
    somaMedia += media
    print(f"A média resultou em: {media}")
    d += 1
    if(media >= 6):
        print("\nAprovado 😊")
        aprovado+=1
    else:
        print("\nReprovado 😢")
        reprovado += 1
    c += 1

#Médias
print("=" * 20)
print("\nInformações:")
mediaT = somaMedia / aluno
print(f"\nA média total da sala foi de: {mediaT:,.2f}")
print(f"{aprovado} alunos foram aprovados!")
print(f"{reprovado} alunos foram reprovados.")