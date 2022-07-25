# Arreglos , vectores, matrices, listas  

numeros = [] # vector 
edades = [15, 18, 25, 38, 50] # arreglo 5 elmentos
		#   0    1   2   3   4  
# int num[100]; # C++
# num = [] # Python
# Arreglos unidimencionales o Vectores: 
#     longitud definida 
#     un mismo tipo de dato 
#     permite modificar los elementos (agregar, eliminar, insertar)

print (edades[0])

# Arreglos Multidimencionales o Matrices :

#         longitud definida N(Filas) x  M(Columnas)
#         un mismo tipo de dato
#         permite modificar los elementos (agregar, eliminar, insertar)

# mat = [][]

mat1 = [[1,2,3], [4,5,6], [7,8,9]]
mat2 = [ 
		[1,2,3,1], 
		[4,5,6,0], 
		[7,8,9,5] 
		]  #  3 Filas x 4 Columnas

print(mat1[1][2])
print(mat2[1][3])
print(mat2[2])

# listas python : 
#         multiples tipos de datos 
#         longitud variable
#         permite modificar los elementos (agregar, eliminar, insertar)

lista = []
lista = [38, "Diego", True, [3.14, 5.1], (1,2,3)]

print (lista[1][2])

# como llenar un vector y matriz

v1 = []

v1.append("Robinson")
v1.append("Raul")
v1.append("Alexandra")
print (v1)

v2 = []
# for i in range(5):
#     x = input("Ingrese un nombre: ")
#     v2.append(x)
# print (v2)

# Matrices
mat = []
y = 0
for i in range(3): # 3 filas
	mat.append([])
	for j in range(4): # 4 columnas
		y += 1 # incremento 1 y = y + 1
		mat[i].append(y)

# [ 1, 2 , 3 , 4 ]
# [ 5, 6 , 7 , 8 ]
# [ 9, 10, 11, 12]
print ("------- Matrices --------")
print (mat)

print ("------- Imprime la Matriz mat --------")
# Procedimiento Imprime la Matriz mat
def imprimir_matriz(mat):
	for i in range(len(mat)):
		for j in range(len(mat[i])):
			print (mat[i][j])

imprimir_matriz(mat) # llama al procedimiento imprimir_matriz
