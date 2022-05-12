
num = int(input("Digite um número: "))
while True:
    if(num < 9 or num > 0):
        break
    else:
        print("❌ ERRO!")
        num = int(input("Digite um número novamente: "))

max = 9
min = 1
primo = True
primo2 = True
tiraum = 0

for i in range(1, num):
    min *= 10
    max = (max*10) + 9

for j in range(min, max+1):
    for k in range(2,(j//2)+1):
        if(j%k==0):
            primo = False
            break
    if(primo):
        tiraum = j
        for l in range(1,num):
            tiraum = tiraum//10
            if tiraum == 1:
                primo2 = False
                break
            for m in range(2, (tiraum // 2) + 1):
                if (tiraum % m == 0):
                    primo2 = False
        if(primo2):
            print(j)
        else:
            primo2 = True
    else:
        primo = True

