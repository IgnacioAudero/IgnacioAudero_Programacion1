# 12.	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

from functions_tps import phrase_dictionary

phrase = input('Escriba una frase: ')
phrase_in_dictionary = phrase_dictionary(phrase)

for word in phrase_in_dictionary:
    print(f'Palabra: {word}\nCantidad de letras: {phrase_in_dictionary[word]}\n')