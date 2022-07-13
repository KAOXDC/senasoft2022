# -----------
# Diseñar un algoritmo en el que a partir de una fecha introducida por teclado con el formato DIA, MES, AÑO, se obtenga la fecha del dia siguiente. 
# Autor : Diego Prado
# version : 1.0
# -----------

# day = int(input("ingrese el día : "))
# month = int(input("ingrese el mes : "))
# year = int(input("ingrese el año : "))
day = 31 
month = 12
year = 2021

month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
bisiesto = False

# calculo del año bisiesto
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            month_days[1] = 29
            bisiesto = True
        else:
            bisiesto = False
    else:
        month_days[1] = 29
        bisiesto = True

if bisiesto == False and month == 2 and day > 28 and day >= 1: 
    print("el año no es bisiesto y el dia no es valido para el mes")
elif bisiesto and month == 2 and day > 28:
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")

for i in range(len(month_days)):
    if month - 1 == i:
        if day >= 1 and day < month_days[i]:
            day += 1
            break
        else:
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1
            break


print("la fecha final es : ", day, "/", month, "/", year)     
    

print(False and True or True and False or True)