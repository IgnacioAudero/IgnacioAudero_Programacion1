
#? 7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde

print('INGRESAR UNA CANTIDAD DE MINUTOS Y MOSTRARE CUANTAS HORAS SON.\n')

minutes = int(input('Minutos: '))
hour = int(minutes / 60)
minutes_excess = minutes % 60

print(f'{minutes} minutos son {hour} horas y {minutes_excess} minutos')