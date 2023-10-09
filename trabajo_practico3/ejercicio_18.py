# 18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión
# comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números
# anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

print('SUCESION FIBONACCI')

numb1 = 0
numb2 = 1
print(numb1)
for i in range(9):
    next = numb1 + numb2
    print(next)
    numb1 = numb2
    numb2 = next