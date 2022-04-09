#Caixa de supermercado - Ler os valores e as quantidades de produtos que
# se encera se 0 for digitado

totalCompra = 0

while True:
    preco = float(input("Preço do produto >> "))

    if preco == 0:
        break
    else:
        qtProd = int(input("Quantidade do produto >> "))
        totalCompra += preco * qtProd
print(f"\nO total da compra é {totalCompra}")


