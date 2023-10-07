# 4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:
# candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
# Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el
# partido [color del candidato elegido].
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles,
# indicar ‘Opción errónea.’

print('BIENVENIDO A LAS ELECCIONES\n')

print('LOS CANDIDATOS SON LOS SIGUIENTES')
print('Partido Rojo')
print('Partido Verde')
print('Partido Azul\n')

print('Escriba A si desea votar al Partido Rojo')
print('Escriba B si desea votar al Partido Verde')
print('Escriba C si desea votar al Partido Azul')
voto = input('Ingrese su voto: ').upper()

if voto == 'A':
    print('Usted ha votado por el Partido Rojo!')
elif voto == 'B':
    print('Usted ha votado por el Partido Verde!')
elif voto == 'C':
    print('Usted ha votado por el Partido Azul!')
else:
    print('Opcion erronea.')