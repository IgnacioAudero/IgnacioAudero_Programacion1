# 17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje
# diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno
# de esos, imprimir otro mensaje.

day = input('Ingrese un dia de la semana: ').lower()

days = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')

if day in days:
    if day == 'lunes':
        print('Buen dia, a trabajar que arranco la semana!')
    elif day == 'viernes':
        print('Buen dia, vamos que ya es viernes!')
    elif day == 'sabado' or day == 'domingo':
        print('Buen dia, que tengas un buen fin de semana!')
    else:
        print('Buen dia.')
else:
    print('Dia incorrecto.')