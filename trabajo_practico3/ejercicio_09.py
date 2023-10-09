# 9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al
# usuario por la contraseña hasta que introduzca la contraseña correcta.

password = input('Ingrese su contraseña: ')

while True:
    validate_password = input('Confirme su contraseña: ')

    if validate_password == password:
        print('Las contraseñas coinciden!!')
        break
    else:
        print('Incorrecto, intente nuevamente.')