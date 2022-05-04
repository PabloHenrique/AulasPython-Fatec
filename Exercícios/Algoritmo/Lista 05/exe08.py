#Ler 3 números e ordena-los em ordem crescente

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))
c = int(input("Informe outro número: "))

if b>a and b>c:
	troca = c
	c = b
	b = troca
else:
	if a>c:
		troca = c
		c = a
		a = troca
if a>b:
	troca = b
	b = a
	a = troca
print(f"Os números em ordem crescente são {a}, {b}, {c}")