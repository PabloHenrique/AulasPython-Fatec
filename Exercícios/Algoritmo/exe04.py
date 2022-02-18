#Ler um preço e informar o valor dele com desconto de 10%

preco = float(input("Digite o preço do produto: "))
novoPreco = preco - (preco * 10/100)

print(f"Com o desconto, o preço do produto é: {novoPreco}")