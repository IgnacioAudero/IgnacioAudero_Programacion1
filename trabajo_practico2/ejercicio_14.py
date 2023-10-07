# 14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
# Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los
# números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a

print('Ingresar valores para a y b para resolver la siguiente ecuacion: x = -b / a')

a = float(input('Ingrese un valor para a: '))
b = float(input('Ingrese un valor para b: '))

if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones (todos los números son solución).")
    else:
        print("La ecuación no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación es x = {x}")