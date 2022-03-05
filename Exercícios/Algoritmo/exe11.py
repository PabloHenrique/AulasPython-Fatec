#Ler duas notas, calcular a média e verificar a situação

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if(media > 7):
    print(f"Sua média resultou em: {media}. Portanto, você foi aprovado!")
else:
    print(f"Sua média resultou em: {media}. Portanto, você foi reprovado!")