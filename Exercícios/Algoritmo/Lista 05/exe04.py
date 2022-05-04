#Ler o valor da compra e aplicar o desconto adequado

compra = float(input("Informe o valor da compra: "))

if compra >= 500.00:
	valor_desconto = 0.2 * compra
else:
	if compra >= 200.00:
		valor_desconto = 0.15 * compra
	else:
		valor_desconto = 0.1 * compra

valor_total = compra - valor_desconto
print("Compra: ", compra)
print("Desconto: ", valor_desconto)
print("Total a pagar: ", valor_total)