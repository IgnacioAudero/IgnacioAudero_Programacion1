
#? 8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones

basic_salary = float(input('Ingrese su sueldo base: '))
sale1 = float(input('Ingrese el valor de la primer venta: '))
sale2 = float(input('Ingrese el valor de la segunda venta: '))
sale3 = float(input('Ingrese el valor de la tercer venta: '))

commission1 = sale1 * 0.1
commission2 = sale2 * 0.1
commission3 = sale3 * 0.1

final_salary = basic_salary + commission1 + commission2 + commission3

print(f'El salario final es de {final_salary}$')