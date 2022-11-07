def elevado(b, e):
    if e == 0:
        return 1
    return b * elevado(b, e-1)


print('Informe a base e o expoente para calcular a potência')
base = int(input('Base >> '))
expo = int(input('Expoente >> '))
print(f'{base} elevado a {expo} é {elevado(base, expo)}')