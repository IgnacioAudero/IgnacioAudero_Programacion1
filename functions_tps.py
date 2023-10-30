import math

def dni_validator(dni):
    if len(str(dni)) == 7 or len(str(dni)) == 8:        # Evalua si la longitud del DNI es igual a 7 u 8
        return True
    else:
        return False

def last_word_len(phrase):
    phrase = phrase.split()     # Separamos la frase usando los espacios

    last_word = phrase[-1]      # Le asignamos a la variable ultima palabra el indice -1 de la frase separada

    return len(last_word)

def id_generator(full_name, full_name_split, dni):
    surname_len = str(last_word_len(full_name))     # Llama a la funcion que devuelve la ultima palabra de una oracion y asi obtiene el apellido del nombre completo
    dni = str(dni)      # Casteamos el dni a string para poder tomar los primeros 3 digitos
    name = str(full_name_split[0])      # Casteamos a string el primer indice del nombre separado segun los espacios

    return name.capitalize() + surname_len + dni[:3]        # Concatenamos para obtener el id personalizado

def multiple_number(number1, number2):
    if number1 % number2 == 0:
        return 0
    elif number2 % number1 == 0:
        return 1
    else:
        return -1

def temperature_median(max_temperature, min_temperature):
    return (max_temperature + min_temperature) / 2

def add_space(sentence):
    sentence_modify = ' '.join(sentence)
    return sentence_modify

def find_max_min(list):
    max_number = max(list)      # Usando max() encontramos el numero mas grande de la lista
    min_number = min(list)      # Usando min() encontramos el numero mas chico de la lista
    return max_number, min_number

def area_perimeter(radius):
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return area, perimeter

def login(user, password, attempts):
    if user == 'usuario1' and password == 'asdasd':
        return True, attempts
    else:
        attempts -= 1
        return False, attempts

def calculate_discounts(shopping_cart):
    final_price = 0

    for price in shopping_cart:
        if shopping_cart[price] == 0:
            final_price += price
        else:
            discount = shopping_cart[price] / 100
            price_discount = price * discount
            final_price += price - price_discount

    return final_price

def add_iva(price_products, calc_iva):
    iva_apply_list = []
    for price in price_products:
        iva_apply_list.append(calc_iva(price))
    return iva_apply_list

def calc_iva(price):
    return price + (price * 0.21)

def phrase_dictionary(phrase):
    dictionary_phrase = {}
    phrase_list = phrase.split()

    for word in phrase_list:
        dictionary_phrase[word] = len(word)

    return dictionary_phrase

def calculate_module(vector):
    addition = sum(component ** 2 for component in vector)
    module = math.sqrt(addition)
    return module

def prime_number(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

def count_digit(number, digit):
    number = str(number)
    counter = 0
    for char in number:
        if digit == char:
            counter += 1
    return counter

def addition_digit(number):
    addition_number = 0
    while number != 0:
        digits = number % 10
        number //= 10
        addition_number += digits

    return addition_number

def bubble_sort(number_list):
    swap = True

    while swap:
        swap = False
        for i in range(len(number_list) - 1):
            if number_list[i] > number_list[i + 1]:
                number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]
                swap = True

    return number_list

def bubble_sort_descending(number_list):
    swap = True

    while swap:
        swap = False
        for i in range(len(number_list) - 1):
            if number_list[i] < number_list[i + 1]:
                number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]
                swap = True

    return number_list

def selection_sort(word_list):
    for i in range(len(word_list)):
        lowest = i
        for j in range(i + 1, len(word_list)):
            if word_list[j] < word_list[lowest]:
                lowest = j
        word_list[i], word_list[lowest] = word_list[lowest], word_list[i]

    return word_list
def insertion_sort(word_list):
    for i in range(1, len(word_list)):
        word = word_list[i]
        j = i - 1
        while j >= 0 and len(word) < len(word_list[j]):
            word_list[j + 1] = word_list[j]
            j -= 1
        word_list[j + 1] = word
    return word_list

def counter_digit(number):
    if number < 10:
        return 1
    else:
        return 1 + counter_digit(number // 10)

def even(num):
    if num == 0:
        return True
    else:
        return odd(num - 1)

def odd(num):
    if num == 0:
        return False
    else:
        return even(num - 1)

def find_higher(number_list):
    if len(number_list) == 1:
        return number_list[0]
    else:
        is_higher = find_higher(number_list[1:])

        if number_list[0] > is_higher:
            return number_list[0]
        else:
            return is_higher

def duplicate_list(number_list, duplicate):
    if duplicate == 1 or not number_list:
        return number_list
    else:
        return [number_list[0]] * duplicate + duplicate_list(number_list[1:], duplicate)