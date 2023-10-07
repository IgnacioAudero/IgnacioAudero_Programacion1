# 3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A
# continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir
# ‘no hay coincidencia’.

name1 = input('Introduce el nombre de la persona 1: ')
name2 = input('Introduce el nombre de la persona 2: ')

if name1[0].upper() == name2[0].upper():
    print(f'La inicial del nombre "{name1.upper()}" y la inicial del nombre "{name2.upper()}" son iguales!!')
else:
    print(f'La inicial del nombre "{name1.upper()}" y la inicial del nombre "{name2.upper()}" no son iguales.')