#Ler a idade do participante e definir a sua categoria

idade = int(input("Informe a idade do participante: "))

if idade <= 8:
	print("Categoria Infantil A")
else:
	if idade < 13:
		print("Categoria Infantil B")
	else:
		if idade < 18:
			print("Categoria Juvenil A")
		else:
			if idade < 21:
				print("Categoria Juvenial B")
			else:
				print("Categoria Senior")