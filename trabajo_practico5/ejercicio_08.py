# 8.	Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función
# en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

from functions_tps import area_perimeter

while True:
    radius = float(input('Ingrese el radio de la circunferencia: '))
    if radius <= 0:
        print('El radio no puede ser 0 o negativo, intente nuevamente.\n')
    else:
        break

area, perimeter = area_perimeter(radius)

print(f'Area de la circunferencia = {area}')
print(f'Perimetro de la circunferencia = {perimeter}')