v1 = [] #15 elementos
v2 = [] #15 elementos
v3 = [] #15 elementos
i = 0 # indice de los vectores
# v1 = [7, 4, 6, 10, 5]
# v2 = [12, 4, 16, 100, -5]

## CAMBIAR LISTA A VECTOR

while True:
	N = int(input("Ingrese el numero de elementos: ")) #15 elementos 0 - 14
	if N > 0 and N < 15:
		break
	else: #fuera del rango del indice de los arreglos
		continue   

# cargar el vector v1
while True:
	num = int(input("Ingrese el numero: V1["+ str(i) + "]: " )) # numeros enteros entre 1 y 30 
	if num >=1 and num <=30:
		v1.append(num)
		i += 1 
		if i == N:
			i = 0
			break
print("------------")
# cargar el vector v2
while True:
	num = int(input("Ingrese el numero: V2["+ str(i) + "]: " )) # numeros enteros entre 1 y 30 
	if num >=1 and num <=30:
		v2.append(num)
		i += 1 
		if i == N:
			i = 0
			break

# # metodo de burbuja
# ordenar el vector v1
for i in range(1,len(v1)):
	for j in range(0,len(v1)-i):
		if(v1[j+1] < v1[j]):
			aux=v1[j]
			v1[j]=v1[j+1]
			v1[j+1]=aux


# ordenar el vector v2
for i in range(1,len(v2)):
	for j in range(0,len(v2)-i):
		if(v2[j+1] < v2[j]):
			aux=v2[j]
			v2[j]=v2[j+1]
			v2[j+1]=aux

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
v3 = v1
for i in range(len(v1)):
	v3.append(v2[i])

print (v3)		

# ordenar el vector v3
for i in range(1,len(v3)):
	for j in range(0,len(v3)-i):
		if(v3[j+1] < v3[j]):
			aux=v3[j]
			v3[j]=v3[j+1]
			v3[j+1]=aux

print (v3)