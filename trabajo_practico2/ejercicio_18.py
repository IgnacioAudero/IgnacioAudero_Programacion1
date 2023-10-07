# 18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
# La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y
# mostrar esta cantidad.
# Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas
# laborales comunes.

hours_worked = int(input('Ingresar cuantas horas trabajo en el mes: '))
hour_wage = float(input('Ingresar cuanto te pagan por hora: '))

if hours_worked > 48:
    extra_hour = hours_worked - 48
    print(f'Usted hizo {extra_hour} horas extras.')
    salary = 48 * hour_wage
    final_salary = salary + ((extra_hour * hour_wage) * 1.1)
    print(f'El salario a cobrar es de ${final_salary}')
else:
    final_salary = hour_wage * hours_worked
    print(f'El salario a cobrar es de ${final_salary}')