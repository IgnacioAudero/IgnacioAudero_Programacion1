
#? 10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#?   •	    55% del promedio de sus tres calificaciones parciales.
#?   •	    30% de la calificación del examen final.
#?   •	    15% de la calificación de un trabajo final.

print('Calcular su calificacion final.')

exam1 = float(input('Ingrese el resultado del primer parcial: '))
while exam1 > 10 or exam1 < 0:
  print('Error, calificacion no valida. Ingrese la calificacion nuevamente.')
  exam1 = float(input('Ingrese el resultado del primer parcial: '))

exam2 = float(input('Ingrese el resultado del segundo parcial: '))
while exam2 > 10 or exam2 < 0:
  print('Error, calificacion no valida. Ingrese la calificacion nuevamente.')
  exam2 = float(input('Ingrese el resultado del segundo parcial: '))

exam3 = float(input('Ingrese el resultado del tercer parcial: '))
while exam3 > 10 or exam3 < 0:
  print('Error, calificacion no valida. Ingrese la calificacion nuevamente.')
  exam3 = float(input('Ingrese el resultado del tercer parcial: '))

final_exam = float(input('Ingrese el resultado del examen: '))
while final_exam > 10 or final_exam < 0:
  print('Error, calificacion no valida. Ingrese la calificacion nuevamente.')
  final_exam = float(input('Ingrese el resultado del examen final: '))

final_job = float(input('Ingrese el resultado del trabajo final: '))
while final_job > 10 or final_job < 0:
  print('Error, calificacion no valida. Ingrese la calificacion nuevamente.')
  final_job = float(input('Ingrese el resultado del trabajo final: '))

average_exam = (exam1 + exam2 + exam3) / 3
final_mark = (average_exam * 0.55) + (final_exam * 0.3) + (final_job * 0.15)

print(f'La calificacion final de la materia algoritmos es de {final_mark}')