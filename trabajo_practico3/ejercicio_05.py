# 5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número
# de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

money_invest = float(input('Ingrese la cantidad de dinero a invertir: '))
interest = float(input('Ingrese el interes anual: '))
year_invest = int(input('Cuantos años vas a invertir el dinero? '))

if interest <= 0:
    print('Interes no valido.')
elif year_invest <= 0:
    print('Año ingresado no valido.')
else:
    for year in range(1, year_invest + 1):
        money_invest += money_invest * (interest / 100)
        print(f'Interes generado en el año {year} es de ${money_invest:.2f}')