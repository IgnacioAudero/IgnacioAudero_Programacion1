# 19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la
# cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades
# que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar
# que las cantidades ingresadas sean positivas.

print('ALCANCIA')

while True:
    amount_money_save = int(input('Ingrese la cantidad de dinero que deseas ahorrar: '))
    if amount_money_save <= 0:
        print('La cantidad de dinero que deseas ahorrar tiene que ser mayor a 0.')
    else:
        break
money_box = 0
while True:
    money = int(input('Cuanto dinero deseas ingresar? '))
    if money < 0:
        print('La cantidad de dinero ingresado no puede ser un numero negativo.')
        continue

    money_box += money
    if money_box >= amount_money_save:
        print(f'Felicidades, tu objetivo era ahorrar ${amount_money_save} y ahorraste ${money_box}')
        break
    else:
        print(f'Ingresaste ${money}, llevas ahorrado ${money_box}')
        print(f'Te faltan ${amount_money_save - money_box} para llegar al objetivo que es ahorrar ${amount_money_save}')