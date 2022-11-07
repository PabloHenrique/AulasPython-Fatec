'''
3.	A expressão em Python, m % n, resulta o resto de m ao dividir
por n. Defina o máximo divisor comum (MDC) de dois inteiros, x e y,
por:
mdc(x,y) = y			se (y<=x && x%y==0)
mdc(x,y) = mdc(y,x)		se (x<y)
mdc(x,y) = mdc(y,x%y)	caso contrário

Escreva um programa em Python com uma função recursiva para
calcular mdc(x,y).
'''

def mdc(x, y):
    if x >= y and x % y == 0:
        return y
    if x < y:
        return mdc(y, x)
    return mdc(y, x % y)

print("Informe dois números para cálculo do MDC")
m = int(input("1º valor -> "))
n = int(input("2º valor -> "))
print(f"O MDC entre {m} e {n} é {mdc(m,n)}")