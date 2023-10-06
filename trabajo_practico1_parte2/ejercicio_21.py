
#? 21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
#? Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
#? Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.

print('\nVIAJE EN MOTO\n')

km_liter = float(input('Ingresar cuantos kilometros puede recorrer su moto con 1 litro de combustible: '))
tank_liter = float(input('Ingrese que capacidad en litros tiene el tanque de la moto: '))
journey_km = float(input('Ingresar cuantos kilometros en total recorreran en el viaje: ')) 

tanks_necesary = journey_km / km_liter
tanks_necesary = int(tanks_necesary) + 1 #esto se hace para redondear los tanques necesarios para arriba.

print(f'Se necesitan {tanks_necesary} tanques de combustible para realizar el viaje de {journey_km} KM')