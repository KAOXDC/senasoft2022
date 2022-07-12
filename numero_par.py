# calcular si un numero es par o impar usando cadenas de texto
# Autor: Diego Prado
# Fecha: 12/07/2022
# Version: 1.0
# --------------------------------------------------------------------------------

print("-------")
print("Programa para saber si un numero es par o impar")
x = input("ingrese un numero : ")
pares = [0,2,4,6,8]
if x[len(x)-1] == '0' :
    encontro = "NEUTRO"
else:
    # for recorre la lista de pares
    for i in pares:
        if x[len(x)-1] == str(i):
            encontro = "PAR"
            break # rompe el ciclo cuando se encuanta el numero en la lista
        else:
            encontro = "IMPAR"
# evauar si el numero es par, impar o neutro
if encontro == "NEUTRO":
    print("el CERO ES NEUTRO")
elif encontro == "PAR":
    print("es par")
elif encontro == "IMPAR":
    print("es IMPAR")

