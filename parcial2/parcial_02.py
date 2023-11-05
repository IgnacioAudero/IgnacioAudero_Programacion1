from parcial_02_functions import is_mutant

print('BIENVENIDO A SU VERIFICADOR DE ADN\n'
      'Porfavor ingrese las letras A, T, C o G\n')

dna = []        # Lista que contenera el adn vacia

for i in range(6):      # Bucle para llenar la lista adn con 6 elementos

    row_dna = []        # Lista llamada fila que va a contener las letras ingresadas

    for j in range(6):      # Bucle para llenar cada elemento de la lista adn con 6 elementos y asi crear una matriz de 6x6

        while True:     # Bucle que verifica que la letra ingresada sea valida
            letter = input('Ingrese valor del ADN: ').upper()

            if letter not in 'ATCG' or len(letter) != 1:        # Si la letra no es correcta o si se ingresa mas de una letra el bucle continua
                print('\nERROR.\n'
                      'Usted no ingreso una letra valida o ingreso mas de una letra, intente nuevamente.\n')

            else:       # Si la letra ingresada es valida la agrega a la lista fila y corta el bucle que verifica la letra
                print(f'Valor {letter} cargado correctamente.\n')
                row_dna.append(letter)
                break

    dna.append(row_dna)     # Agrega la lista fila que contiene las letras ingresadas a la lista contenedora del adn

# Mostrar matriz de adn ingresada
print('\nADN INGRESADO:')
for row in dna:
    for element in row:
        print(element, end=' ')
    print()

# Resultado final
print('\nES MUTANTE O NO?')
mutant, counter = is_mutant(dna)

if mutant:
    print('\nEl ADN ingresado es MUTANTE.\n'
          f'Se encontraron {counter} secuencias.')
else:
    print('\nEl ADN ingresado NO es MUTANTE.')

# Si ingresamos la siguiente secuencia:
# adn = [[ATGCGA],[CAGTGC],[TTATGT],[AGAAGG],[CCCCTA],[TCACTG]]
# Tendremos como resultado que el adn es mutante y se encontraron 3 secuencias.

# Si ingresamos la siguiente secuencia:
# adn = [[ATGCGA],[CAGTGC],[TTATTT],[AGACGG],[GCGTCA],[TCACTG]]
# Tendremos como resultado que el adn no es mutante.