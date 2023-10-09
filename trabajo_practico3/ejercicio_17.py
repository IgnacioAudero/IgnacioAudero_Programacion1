# 17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que
# aparecen en esa frase (sin repetirlas).

phrase = input('Ingresar una frase: ')

vowels = ['a', 'e', 'i', 'o', 'u']
amount_vowels = 0

for i in range(len(phrase)):
    if phrase[i] in vowels:
        amount_vowels += 1

print(f'La frase "{phrase.upper()}" tiene {amount_vowels} vocales')