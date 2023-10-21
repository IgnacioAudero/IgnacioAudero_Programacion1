def addition_digit(number):
    addition_number = 0
    while number != 0:
        digits = number % 10
        number //= 10
        addition_number += digits

    return addition_number

def replace_letter(phrase, phrase_hidden, letter):

    for i in range(0, len(phrase)):     # Recorre la frase y si las letras coinciden reemplaza el guion bajo por la letra en la posision debida en la frase oculta
        if letter == phrase[i]:
            phrase_hidden = phrase_hidden[:i] + letter + phrase_hidden[i + 1:]

    return phrase_hidden