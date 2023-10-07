# 12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde
# ese año o cuántos años faltan para llegar a ese año.

current_year = int(input('Ingrese el año actual: '))
addmitted_year = int(input('Ingrese un año cualquiera: '))

if current_year < addmitted_year:
    year = addmitted_year - current_year
    print(f'Faltan {year} año/s para el año {addmitted_year}')
elif current_year > addmitted_year:
    year = current_year - addmitted_year
    print(f'Pasaron {year} año/s desde el {addmitted_year}')
elif current_year == addmitted_year:
    print('El año ingresado es el mismo que el año actual.')