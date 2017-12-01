def add_contacts(phone_book, name, phone):
    phone_book[name] = phone


def show_contacts(phone_book):
    print("-")
    if phone_book == {}:
        print("Lista de contactos vacia")
    for name, number in phone_book.items():
        print("{}: {}".format(name, number))
    print("-")
    input("Pulsa una tecla para volver al menú: ")


def remove_contacts(phone_book, name):
    del(phone_book[name])


def menu():
    phone_book = {}
    while True:
        print("=========================")
        print("|                        |")
        print("| 1. Mostrar contactos   |")
        print("| 2. Añadir contactos    |")
        print("| 3. Eliminar contactos  |")
        print("| 4. Salir               |")
        print("|                        |")
        print("=========================|")
        option = input("Seleccione una opción del menú:  ")
        option = int(option)
        if option == 1:
            show_contacts(phone_book)
        if option == 2:
            name = input("Escribe nuevo contacto: ")
            if name in phone_book:
                print("El usuario no existe")
            else:
                phone = input("Escribe número de teléfono de nuevo contacto: ")
                add_contacts(phone_book, name, phone)
        if option == 3:
            name = input("Escriba el contactos que quieres eliminar: ")
            if name in phone_book:
                remove_contacts(phone_book, name)
            else:
                print("El nombre no esta en la agenda")
        if option == 4:
            print("Saliendo del programa de agenda de contacto")
            break
menu()
