numero = input('Informe um número >>> ')

numero = numero.replace(',','.')

if numero.replace('.','').isdigit():
    numero = float(numero)
    print('Número digitado', numero)
else:
    print('Não é um número')