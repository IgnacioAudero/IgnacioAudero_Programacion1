# 4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los
# años en ese rango, que sean bisiestos y múltiplos de 10.
# Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por
# 100, excepto que también sea divisible por 400.

while True:
    year1 = int(input('Ingresar el primer año: '))
    year2 = int(input('Ingresar el segundo año: '))
    if year1 < 0 or year2 < 0:
        print('No se pueden ingresar años negativos.')
        continue
    else:
        break

year_higher = max(year1, year2)
year_lower = min(year1, year2)

for year in range(year_lower, year_higher + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 10 == 0):
        print(year)