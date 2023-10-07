# 20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4)
# notas, es mayor o igual a 6; caso contrario saldrá desaprobado.

exam1 = float(input('Ingrese la primer nota: '))
exam2 = float(input('Ingrese la segunda nota: '))
exam3 = float(input('Ingrese la tercera nota: '))
exam4 = float(input('Ingrese la cuarta nota: '))

average = (exam1 + exam2 + exam3 + exam4) / 4
if average >= 0 and average <=10:
    if average >= 6:
        print(f'Felicidades, usted aprobo la materia con un promedio de {average}')
    else:
        print(f'Lo lamento, usted recurso la materia con un promedio de {average}')
else:
    print('Usted ingreso alguna nota mal.')