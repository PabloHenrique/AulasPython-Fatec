'''
    Faça um programa em Python que leia uma String e dois caracteres.
    Troque todas as ocorrências do primeiro caractere (podendo ser maiúsculo ou minúsculo)
    pelo segundo e imprima a quantidade de vezes que o caractere foi substituído.
'''

texto = input('Informe um texto >>> ')
carac_1 = input('Informe o 1º caractere >>> ')
carac_2 = input('Informe o 2º caractere >>> ')

qt_carac = texto.upper().count(carac_1.upper())
texto = texto.replace(carac_1.upper(), carac_2)
texto = texto.replace(carac_1.lower(), carac_2)

print(texto)
print(f'Foram substituídos {qt_carac} caracteres')

