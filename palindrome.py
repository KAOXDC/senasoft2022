# 1 Averiguar si una palabra es un palindromo. 
# Un palíndromo es una palabra que se lee igual 
# de izquierda a derecha que de derecha a izquierda, 
# como por ejemplo, 'radar', 'oso'

# "h" + "o" + "l" + "a"
# 1	   2	 3	   4  ELEMENTOS
# 0    1 	 2     3  INDICE / POSICION
# "hola"
# 'hola'

# print (c[0] + " " + c[5])

# print("-------")

# for elemento in c: # elemento de la cadena
# 	print (elemento)
# print("-------")
						
# for indice in range(11): #elemento numero entero
# 	print (c[indice])

# # como saber cuantos elementos tengo sin usar len 
# c = "radar"
# c = "narran"

c = input("ingrese una palabra : ")
contador = 0
for indice in c: #elemento numero entero
	contador = contador + 1
print (contador) # 5

for i in c:
	if i == c[contador - 1]:
		#print ("coincide con la letra " + i + c[contador - 1])
		contador = contador - 1
		if contador == 0:
			print ("la palabra  "+ c + "  es palindrome")
	else:
		print("la palabra "+ c + " NO es palindrome")
		break
