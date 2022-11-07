'''
4.	Considere a função Comb(n,k), que representa o número de
grupos distintos com k pessoas que podem ser formados a partir
de n pessoas. Por exemplo, Comb (4,3) = 4, pois com 4 pessoas
(A, B, C e D), é possível formar 4 diferentes grupos:
ABC, ABD, ACD e BCD. Sabe-se:
Comb (n,k) = n		se k==1
Comb (n,k) = 1		se k==n
Comb(n,k) = Comb(n-1, k-1) + Comb (n-1, k)  caso contrário

Escreva um programa em Python com uma função recursiva para Comb (n,k).
'''

def comb(n, k):
    if k == 1:
        return n
    if k == n:
        return 1
    return comb(n-1, k-1) + comb(n-1, k)

print("Informe o números de pessoas que podem e a quantidade por grupo, "
      "\npara calcular quantos grupos distintos pode-se formar")
pessoas = int(input("Número de pessoas -> "))
qt = int(input("Quantidade por grupo -> "))
if qt > pessoas:
    print("A quantidade de pessoas por grupo não pode ser maior que a quantidade total de pessoas")
else:
    print(f"Serão formados {comb(pessoas, qt)} grupos")
