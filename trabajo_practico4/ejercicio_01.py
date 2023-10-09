# 1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas
# convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.

sequence = []

while True:
    phrase = input("Ingrese una línea o dejar en blanco para finalizar: ")
    if phrase == "":
        break
    sequence.append(phrase)

print("Líneas en mayúsculas:")
for phrase in sequence:
    print(phrase.upper())