# 13-	Escribir un programa que muestre el eco de to,do lo que el usuario
#  introduzca hasta que el usuario escriba “salir” que terminará.

phrase = ''

while phrase.lower() != "salir":
    phrase = input("Escribe una frase o escriba salir para terminar el programa: ")
    if phrase.lower() != "salir":
        print(phrase)