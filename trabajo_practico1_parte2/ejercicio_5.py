
#? 5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

#? a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
#! Solo podemos pasarle un argumento a la funcion input

A = input("¿Cuál es tu canción favorita?")

#? b)	precio = input(“Precio: “)
#?     total = precio + (precio * 0.1)
#! El valor por defecto que devuelve un input es str, si no casteamos a float/int no podemos hacer operaciones matematicas

precio = float(input("Precio: "))
total = precio + (precio * 0.1)

#? c)	edad = int(input(“Edad: “))
#?     print(tu edad es, edad)
#! El mensaje y las variables tienen que estar separadas, el mensaje entre comillas y la variable concatenada con una coma

edad = int(input("Edad: "))
print("Tu edad es", edad)

#? d)	edad = int(input(“Edad: “))
#?      print(“Veamos si tu edad es 18…”, edad=18)
#! no debemos darle valor a la variable dentro del print

edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad)
