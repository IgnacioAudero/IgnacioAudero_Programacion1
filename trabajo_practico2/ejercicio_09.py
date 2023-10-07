# 9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está
# formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por
# el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
# que le corresponde.

print('Ingrese su nombre y sexo para ver si va al grupo A o al grupo B.\n')

name = input('Ingrese su nombre: ').lower()
sex = input('Ingrese su sexo (hombre o mujer): ').lower()

if sex == 'hombre' or sex == 'mujer':
    if (name[0] <= 'm' and sex == 'mujer') or (name[0] >= 'n' and sex == 'hombre'):
        print('Usted pertenece al grupo A')
    else:
        print('Usted pertenece al grupo B')
else:
    print('Sexo incorrecto.')