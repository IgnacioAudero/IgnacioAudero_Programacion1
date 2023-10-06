
#? 15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B

deperature_time = input("Ingrese la hora de partida (HH:MM:SS): ")
deperature_time = deperature_time.split(':')
deperature_hour = int(deperature_time[0])
deperature_minute = int(deperature_time[1])
deperature_seconds = int(deperature_time[2])

time_trip = int(input('Ingresar el tiempo de viaje en segundos: '))

seconds_arrival = deperature_seconds + time_trip
minutes_arrival = deperature_minute + (seconds_arrival // 60)
hour_arrival = deperature_hour + (minutes_arrival // 60)

minutes_arrival %= 60
seconds_arrival %= 60

hour_arrival %24

print(f'La hora de llegada a la ciudad B es a las {hour_arrival}:{minutes_arrival}:{seconds_arrival}')
