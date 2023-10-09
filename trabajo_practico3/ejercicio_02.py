# 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha
# cumplido (desde 1 hasta su edad).

age = int(input('Ingrese su edad y mostrare todas tus edades anteriores: '))

for numb in range(age + 1):
    print(numb)