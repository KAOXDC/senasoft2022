# print()
# print(print())
# x = "Hola a todos"
# print(x.capitalize())

def hablar(mensaje):
    print(mensaje)

def saludar(nombre):
    print("Hola " + nombre)
    hablar("hola")

def despedir(nombre):
    print("Adiós " + nombre)


saludar("Juan")
# hablar("Hola que tal estás?")
despedir("Juan")

# m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1=[]
m2=[]
n = 3
m = 3
# crear la matriz
def crear_matriz(m1, m2):
    for i in range(n):
        m1.append([])
        m2.append([])
        for j in range(n):
            m1[i].append(0)
            m2[i].append(0)

    imprimir_matriz(m1)
    imprimir_matriz(m2)

# imprimir matriz
def imprimir_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()
    print()

crear_matriz(m1, m2)

# ---------------------
# ------ Factorial de un numero con ciclos -----
f = 4
# Factorial de 4 es : 4 * 3 * 2 * 1 = 24
acum = 1
for i in range (f , 1 , -1):
    acum = acum * i
print (acum)
# ---------------------
# ------ Factorial de un numero con funciones recursivas -----
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print (factorial(f))
# ---------------------

# Consultar Funciones con arg kargs
