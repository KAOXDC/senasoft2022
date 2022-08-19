# -*- utf-8 -*-
class Automovil():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
        self.estado = "Activo"

class Camioneta():
    marca = ""
    modelo = ""
    enmarcha = False
    acelera = False
    frena = False
    estado = "Inactivo"

# Registros de los atributos de la clase Carro
carro1 = Automovil("Mazda", "MX5") # esté es con el contructor de la clase Carro
print (carro1.marca, carro1.modelo)
carro1.marca = "Audi"
print (carro1.marca, carro1.modelo)


carro2 = Camioneta()
print(carro2.marca, carro2.modelo, carro2.estado)
carro2.marca = "Mercedes"
carro2.modelo = "2022"
carro2.estado = "Activo"
print(carro2.marca, carro2.modelo, carro2.estado)


# archivos 

lista = ["Mazda", "Audi", "Mercedes", "BMW"]
dictionary = {
    "modelo": "MX5", 
    "marca": "audi", 
    "estado": "en venta", 
    "precio": "100.000",
    }
# abrir archivo en modo escritura y sino extiste lo crea
archivo = open("archivo.txt", "w") # abre el archivo para escribir

archivo.write("Hola    \t mundo\n")
archivo.write("ñ Ñ á Á é É í Í ó Ó ú Ú")
archivo.write(carro1.marca + "\t\t" + carro1.modelo + "\n" )
archivo.write(carro2.marca + "\t\t" + carro2.modelo + "\n" )
archivo.write(carro1.marca + "\t\t" + carro1.modelo + "\n" )
archivo.write(carro2.marca + "\t\t" + carro2.modelo + "\n" )
for item in lista:
    archivo.write(item + "\n")
archivo.write(str(lista) + "\n" )
archivo.write(str(carro2.acelera) + "\t\t" + str(2) + "\n" )

archivo.write(str(dictionary) + "\n" )  
archivo.write(lista[2] + "\n" )  
archivo.write(dictionary["marca"] + str(dictionary["precio"]) + "\n" )


archivo.close() # cierra el archivo

# leer archivo en modo lectura
archivo = open("archivo.txt", "r") # abre el archivo en modo lectura

print(archivo) # muestra el objeto del archivo
for linea in archivo:
    print(type(linea))
    print(len(linea))

archivo.close() # cierra el archivo