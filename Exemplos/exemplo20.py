               texto = 'Lorem ipsum may be used as a placeholder before final copy is available.'
print(texto)
print(texto.upper().count('P'))

print('='*50)

#caso não encontre retorna -1 (acha o primeiro)
print(texto.upper().find('P'))

print('='*50)

#caso não encontre retorna -1 (acha o ultimo)
print(texto.upper().rfind('P'))

print('='*50)

pos = 0
while pos != -1:
    pos = texto.upper().find('P', pos)
    if pos != -1:
            print(pos)
            pos += 1

print('='*50)

if 'final' in texto:
    print('Texto encontrado')
else:
    print('Texto não encontrado')
