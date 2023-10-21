# 6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un
# espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa
# principal donde se use dicha función.

from functions_tps import add_space

phrase = input('Ingrese una frase: ')
phrase_space = add_space(phrase)
print(phrase_space)