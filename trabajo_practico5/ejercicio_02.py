# 2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las
# palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final
# del string pasado por parámetro.

from functions_tps import last_word_len

sentence = input('Ingrese una oracion: ')

word_len = last_word_len(sentence)      # Llama a la funcion que calcula la longitud de la ultima palabra

print(f'La longitud de la ultima palabra es: {word_len}')