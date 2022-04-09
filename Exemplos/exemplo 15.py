for i in range(24):
    for j in range(60):
        print(f'{i:02}:{j:02}')

print()

for i in range(6):
    for j in range(6):
        print(f'[{i}{j}]', end='')
    print()

print()
for i in range(1,6):
    for j in range(1,i+1):
        print(f'{j}', end=' ')
    print()