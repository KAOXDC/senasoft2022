# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# Programa que muestra las fichas del domino 
# Autor: Diego Prado
# Version: 1.0
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


print("programa muestre las fichas de domino")
# mostrar las fichas de domino
x = 6
y = 6
for i in range(x, -1, -1):
    for j in range(y, -1, -1):
        print("{} {}".format(i, j), end="\t")
    x -= 1
    y -= 1
    print()