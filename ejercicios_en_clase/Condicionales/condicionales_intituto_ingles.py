print('BIENVENIDO AL INSTITUTO DE INGLES')

date = input('Ingrese la fecha en formato "dia, DD/MM": ').lower()
day = date[0 : date.find(',')]
day_number = int(date[date.find(' ') + 1 : date.find('/')])
month = int(date[date.find('/') + 1 :])

list_day = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes'] #lista con los dias de la semana

if day in list_day: 
  if (day_number <= 31 and month <= 12): #evalua el dia y mes ingresado
    if (day == 'lunes' or day == 'martes' or day == 'miercoles'): #nivel inicial, intermedio y avanzado
      students = int(input('Ingrese la cantidad de alumnos: ')) #cantidad de alumnos que asistieron
      exam = input('Se tomaron examenes? Ingrese "S" si tomaron examenes o "N" si no tomaron examenes: ').upper()
      if (exam == 'S'): #evalua si se tomaron examenes o no
        students_pass = int(input('Ingrese la cantidad de alumnos aprobados: '))
        students_no_pass = int(input('Ingrese la cantidad de alumnos desaprobados: '))
        students_addition = students_pass + students_no_pass

        if (students < students_addition):
          print('Se registraron mas alumnos que aprobaron/desaprobaron que la cantidad de alumnos ingresada.')
        else:
          students_average = (students_pass/students_addition) * 100
          print(f'El porcentaje de alumnos aprobados fue de {students_average}%')
      elif (exam == 'N'):
        print('No se tomaron examenes.')
      else:
        print('Opcion incorrecta.')
    elif (day == 'jueves'): #practica hablada
      attendance_average = float(input('Ingrese el porcentaje de asistencia a clase: '))
      if attendance_average > 50.0:
        print("Asistió la mayoría.")
      else:
        print("No asistió la mayoría.")
    else: #ingles para viajeros
      if (day_number <= 7):
        print('COMENZO UN NUEVO CICLO.')
        students_travellers = int(input('Ingrese la cantidad de alumnos ($1500 por alumno): '))
        tariff = students_travellers * 1500
        print(f'Los ingresos totales en este nuevo ciclo es de {tariff}$')
  else:
    print('Dia o mes incorrecto.')
else:
  print('Dia se la semana incorrecto.')
