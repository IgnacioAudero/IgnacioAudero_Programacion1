# 1-Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el
# computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.

computer_year_old = int(input('Ingrese cuantos años tiene su computadora: '))

if computer_year_old <= 2:
    print('Tu computadora es nueva!')
elif computer_year_old > 2:
    print('Tu computadora es vieja, cambiala!')