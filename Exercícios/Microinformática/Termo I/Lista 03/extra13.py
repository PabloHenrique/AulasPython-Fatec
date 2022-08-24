#13. Quadrante
'''
Leia 2 valores com casa decimal (x e y), que devem representar as coordenadas de um ponto em um
plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos
cartesianos ou na origem (x = y = 0).
'''

x = float(input("x >> "))
y = float(input("y >> "))

if x == y == 0:
    print("\nPonto de origem")
elif x == 0:
    print("\nEixo das abscissas")
elif y == 0:
    print("\nEixo das ordenadas")
elif x > 0 and y > 0:
    print("\nQuadrante 01")
elif x < 0 and y > 0:
    print("\nQuadrante 02")
elif x > 0 and y < 0:
    print("\nQuadrante 04")
else:
    print("\nQuadrante 03")


