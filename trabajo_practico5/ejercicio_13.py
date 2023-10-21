# 13.	Escribir una función que calcule el módulo de un vector.'

from functions_tps import calculate_module

print('CALCULAR MODULO DE UN VECTOR.\n')

vector = []

while True:
    component = int(input('Ingrese un componente para el vector o ingrese 0 para no agregar mas elementos: '))

    if component == 0:
        if len(vector) < 2:
            print('El vector necesita al menos dos componentes.')
            continue
        else:
            break
    else:
        vector.append(component)

module = calculate_module(vector)

print(f'El modulo del vector ingresado es {module}')