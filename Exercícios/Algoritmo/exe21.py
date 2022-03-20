#Ler um ano e informar se ele é bissexto

ano = int(input("Digite um ano: "))
if ((ano%400 == 0) or (ano%100 > 0 and ano%4==0)):
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")