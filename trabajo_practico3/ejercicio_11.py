# 11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las
# letras de la palabra introducida empezando por la última.

word = input('Ingrese una palabra: ')

for i in word[::-1]:
    print(i)