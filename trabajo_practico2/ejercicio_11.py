# 11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes
# para cada tipo de pizza aparecen a continuación.
# •	Ingredientes vegetarianos: Pimiento y tofu.
# •	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le
# muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la
# mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
# vegetariana o no y todos los ingredientes que lleva.

print('\nBIENVENIDO A LA PIZZERIA BELLA NAPOLI\n')

print('----------------MENU----------------')
print('1- Pizza vegetariana.')
print('2. Pizza no vegetariana.\n')

menu_option = int(input('Seleccione que tipo de pizza deseas: '))
if menu_option == 1:
    print('\n---------------------PIZZAS VEGETARIANA---------------------')
    print('-------Elija un ingrediente para su pizza vegetariana-------')
    print('[Todas las pizzas vienen con tomate y mozzarella]')
    print('a- Pimiento')
    print('b- Tofu')
    pizza_option = input('Que ingrediente desea elegir? ').lower()
    if pizza_option == 'a':
        print('Su eleccion fue una pizza vegetariana con tomate, mozzarella y pimiento.')
    elif pizza_option == 'b':
        print('Su eleccion fue una pizza vegetariana con tomate, mozzarella y tofu.')
    else:
        print('Opcion incorrecta.')

elif menu_option == 2:
    print('\n---------------------PIZZAS NO VEGETARIANA---------------------')
    print('-------Elija un ingrediente para su pizza no vegetariana-------')
    print('[Todas las pizzas vienen con tomate y mozzarella]')
    print('a- Peperoni')
    print('b- Jamon')
    print('c- Salmon')
    pizza_option = input('Que ingrediente desea agregar? ').lower()
    if pizza_option == 'a':
        print('Su eleccion fue una pizza no vegetariana con tomate, mozzarella y peperoni.')
    elif pizza_option == 'b':
        print('Su eleccion fue una pizza no vegetariana con tomate, mozzarella y jamon.')
    elif pizza_option == 'c':
        print('Su eleccion fue una pizza no vegetariana con tomate, mozzarella y salmon.')
    else:
        print('Opcion incorrecta.')

else:
    print('Opcion no valida')