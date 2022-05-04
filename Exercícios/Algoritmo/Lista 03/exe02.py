#Ler o valor em reais e mostrar a conversão de seu valor para dólar.

reais = float(input("Digite o valor em reais: "))
cotacao = float(input("Qual o valor da cotação do Dolar?"))

dolar = reais * cotacao

print(f"O valor R${reais} em Doláres resultam em: U${dolar}")
