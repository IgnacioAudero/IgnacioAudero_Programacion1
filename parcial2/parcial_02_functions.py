def is_mutant(dna):
    sequense_counter = 0        # Contador de secuencias validas encontradas

    # Bucle que evalua las secuencias horizontales
    for row in dna:
        for start in range(len(dna[0]) - 3):
            sequense = ''       # Cada vuelta del bucle se crea una variable secuancia vacia

            for value in row[start: start + 4]:     # Se le agrega las letras a la variable secuencia
                sequense += value

            if sequense_valid(sequense):        # Llamamos a la funcion que valida la secuencia y si retorna verdadero sumamos 1 al contador de secuencias validas
                sequense_counter += 1

    # Bucle que evalua las secuencias verticales
    for col in range(len(dna[0])):
        for start in range(len(dna) - 3):
            sequense = ''       # Cada vuelta del bucle se crea una variable secuancia vacia

            for i in range(4):      # Se le agrega las letras a la variable secuencia
                sequense += dna[start + i][col]

            if sequense_valid(sequense):        # Llamamos a la funcion que valida la secuencia y si retorna verdadero sumamos 1 al contador de secuencias validas
                sequense_counter += 1

    # Bucle que evalua las secuencias oblicuas
    for start_row in range(len(dna) - 3):       # Diagonal izquierda a derecha
        for start_col in range(len(dna[0]) - 3):
            sequense = ''       # Cada vuelta del bucle se crea una variable secuancia vacia

            for i in range(4):      # Se le agrega las letras a la variable secuencia
                sequense += dna[start_row + i][start_col + i]

            if sequense_valid(sequense):        # Llamamos a la funcion que valida la secuencia y si retorna verdadero sumamos 1 al contador de secuencias validas
                sequense_counter += 1

    for start_row in range(len(dna) - 3):       # Diagonal derecha a izquierda
        for start_col in range(len(dna[0]) - 3):
            sequense = ''       # Cada vuelta del bucle se crea una variable secuancia vacia

            for i in range(4):      # Se le agrega las letras a la variable secuencia
                sequense += dna[start_row + i][start_col + 3 - i]

            if sequense_valid(sequense):        # Llamamos a la funcion que valida la secuencia y si retorna verdadero sumamos 1 al contador de secuencias validas
                sequense_counter += 1

    # Condicional que evalua la cantidad de secuencias encontradas
    if sequense_counter >= 2:
        return True, sequense_counter
    else:
        return False, sequense_counter

def sequense_valid(sequense):       # Funcion que verifica si la secuensia es valida o no
    if sequense == 'AAAA' or sequense == 'TTTT' or sequense == 'CCCC' or sequense == 'GGGG':        # Se evalua si la sentencia enviada es valida para que sea mutante
        return True     # Si es valida retorna verdadero
    else:
        return False    # Si no es valida retorna falso