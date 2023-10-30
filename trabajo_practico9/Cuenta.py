from Persona import Persona

class Cuenta:
    # CONSTRUCTOR
    def __init__(self, owner = Persona(), amount = 0):
        self.owner = owner
        self.amount = amount

    # GETTERS
    def get_owner(self):
        return self.owner

    def get_amount(self):
        return self.amount

    # SETTERS
    def earn(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print('NO SE PUEDE INGRESAR UNA CANTIDAD NEGATIVA.')

    def take_out(self, amount):
        if amount > 0:
            self.amount -= amount
        else:
            print('NO SE PUEDE RETIRAR UNA CANTIDAD NEGATIVA')

    # METODOS
    def show_information(self):
        print('\n------------DATOS DE LA CUENTA------------')
        print(f'Nombre: {self.owner.get_name()}')
        print(f'Edad: {self.owner.get_age()}')
        print(f'DNI: {self.owner.get_dni()}')
        print(f'Dinero en cuenta: {self.amount}')