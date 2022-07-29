v1 = [] #15 elementos
v2 = [] #15 elementos
v3 = [] #15 elementos
i = 0 # indice de los vectores
# v1 = [7, 4, 6, 10, 5]
# v2 = [12, 4, 16, 100, -5]

## CAMBIAR LISTA A VECTOR

# funcion ordenar vector 
def ordenar(vector):
	for i in range(1,len(vector)):
		for j in range(0,len(vector)-i):
			if(vector[j+1] < vector[j]):
				aux=vector[j]
				vector[j]=vector[j+1]
				vector[j+1]=aux
	return vector



while True:
	N = int(input("Ingrese el numero de elementos: ")) #15 elementos 0 - 14
	if N > 0 and N < 15:
		# N = 3 v1 = [0,0,0]
		# N = 3 v2 = [0,0,0]
		for x in range(N):
			v1.append(0)
			v2.append(0)
		break
	else: #fuera del rango del indice de los arreglos
		continue   

# cargar el vector v1
while True:
	num = int(input("Ingrese el numero: V1["+ str(i) + "]: " )) # numeros enteros entre 1 y 30 
	if num >=1 and num <=30:
		v1[i] = num
		#v1.append(num)
		i += 1 
		if i == N:
			i = 0
			break
print("------------")
# cargar el vector v2
while True:
	num = int(input("Ingrese el numero: V2["+ str(i) + "]: " )) # numeros enteros entre 1 y 30 
	if num >=1 and num <=30:
		v2[i] = num
		#v2.append(num)
		i += 1 
		if i == N:
			i = 0
			break

# # metodo de burbuja
# ordenar el vector v1
v1 = ordenar(v1)
# ordenar el vector v2
v2 = ordenar(v2)

print("------------")
print (v1)
print (v2)
print("------------")

for k in range(len(v1)):
    print (v1[k] + v2[k],  end=", ")


# v1 = [7, 4, 6, 10, 5]
# v2 = [12, 4, 16, 100, -5]

# v1 = [4, 5, 6, 7, 10]
# v2 = [-5, 4, 12, 16, 100 ]

# v3 = [4, 5, 6, 7, 10, -5, 4, 12, 16, 100 ]

# Vector 3 para concatenar los vectores v1 y v2
v3 = v1
for i in range(len(v1)):
	v3.append(v2[i])
print ("Vector 3 Concatenado: ", v3)

# ordenar el vector v3
v3 = ordenar(v3)
# print ("Vector 3 ordenado: ", v3)
for i in v3:
	print (i, end=", ")