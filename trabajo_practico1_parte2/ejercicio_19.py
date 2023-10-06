
#? 19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.

day = int(input('Dia: '))
month = int(input('Mes: '))
year = int(input('Año: '))

if len(str(day)) != 2 or len(str(month)) != 2 or len(str(year)) != 4:
  print('Error.')
else:
  print(f'La fecha ingresada es {day}/{month}/{year}')