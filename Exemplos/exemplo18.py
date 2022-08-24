nome = input('Informe um nome >>> ')
qt_letra = 0

for i in nome:
	if i.isalpha():
		qt_letra += 1


print(f'Tem {qt_letra} letras no nome')