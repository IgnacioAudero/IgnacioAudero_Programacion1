# 6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser
# divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

year = int(input('Ingresar un anio y te dire si es bisiesto: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'El anio {year} es anio bisiesto!!')
else:
    print(f'El anio {year} no es anio bisiesto')