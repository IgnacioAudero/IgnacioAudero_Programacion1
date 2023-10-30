from functions_tps import dni_validator

class Persona:
    # CONSTRUCTOR
    def __init__(self, name = '', age = 0, dni = 0):
        self.name = name
        self.age = age
        self.dni = dni

    # GETTERS
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_dni(self):
        return self.dni

    # SETTERS
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print('\nNO SE PUEDE INGRESAR UNA EDAD NEGATIVA.')

    def set_dni(self, dni):
        if dni_validator(dni):
            self.dni = dni
        else:
            print('EL DNI INGRESADO NO ES VALIDO.')

    # METODOS
    def show_datum(self):
        print(f'NOMBRE = {self.name}')
        print(f'EDAD = {self.age}')
        print(f'APELLIDO = {self.dni}')

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False