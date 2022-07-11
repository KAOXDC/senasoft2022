"""14 Determinar el precio de un billete de ida y vuelta en 
ferrocarril, conociendo la distancia a recorrer y sabiendo 
que si el número de dias de estancia es superior a siete y la 
distancia superior a 800 kilómetros el billete tiene una reducción
 del 30%. El precio por kilómetro es de 2,5 dólares."""

distancia = 0
num_dias = 0
billete = 0
DESCUENTO = 30
PRECIO_KM = 2.5

distancia = int(input("ingrese la distancia : "))
num_dias = int(input("ingrese la numero de dias : "))
ida_regreso = distancia * 2

if num_dias > 7 and ida_regreso > 800:
	# calcualar el descuento 
	billete = (ida_regreso * 2.5 ) * 0.7 
	print ("el valor del billete por " + str(num_dias) + " dias, ocn distancia ida y vuelta " + str(ida_regreso) + " km " + " es de " + str(billete) + "$USD")
else:
	# calculo normal de billete
	billete = (ida_regreso * 2.5 ) 
# 	print ("el valor del billete por " + " dias, ocn distancia ida y vuelta " + str(ida_regreso) + " es de " + str(billete) + "$USD")
 	print ("el valor del billete de ida y vuelta %i es de %f $USD" %(ida_regreso, billete))