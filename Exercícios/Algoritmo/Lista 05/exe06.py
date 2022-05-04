#Ler 3 valores, verificar se forma um triângulo e qual seu tipo

a = int(input("Informe um lado do triangulo: "))
b = int(input("Informe outro lado do triangulo: "))
c = int(input("Informe outro lado do triangulo: "))

if a>b and a>c:
	lados_menores = b+c
	maior = a
else:
	if b>c:
		lados_menores = a+c
		maior = b
	else:
		lados_menores = a+b
		maior = c
if lados_menores > maior:
	if a==b and b==c:
		print("Esse é um triangulo equilátero")
	else:
		if c==a or c==b or a==b:
			print("Esse é um triangulo isoceles")
		else:
			print("Esse é um triangulo escaleno")
else:
	print("Esses valores não formam um triangulo")