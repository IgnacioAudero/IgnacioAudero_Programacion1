
#? 1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.

print('CALCULAR AREA Y PERIMETRO DE UN RECTANGULO.\n')

width = int(input('BASE DEL RECTANGULO: '))
height = int(input('ALTURA DEL RECTANGULO: '))

perimeter = (2 * width) + (2 * height)
area = width * height

print(f'PERIMETRO = {perimeter}')
print(f'AREA = {area}')