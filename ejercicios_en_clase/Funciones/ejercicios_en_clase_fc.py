def addition_digit(number, addition_number = 0):
    while number != 0:
        digits = number % 10
        number //= 10
        addition_number += digits

    return addition_number