import math
print("-------------------------------------------------------------------")
print("| (1) Calcular el diámetro de la circunferencia: d = 2 * r)       |")
print("| (2) Calcular el perímetro de la circunferencia: p = 2 * pi * r) |")
print("| (3) Calcular el área del circulo: a = pi * r ** 2)              |")
print("| (4) Salir                                                       |")
print("-------------------------------------------------------------------")
teclado = int(input("Escriba  un número del menú:", ))
# Variable del radio
r = int(input("Escribe el radio:", ))
d = 2 * r
# Variable de la formula del perímetro
p = 2 * math.pi * r
# Variable de la fórmula del área del círculo
a = math.pi * r ** 2
if teclado == 1:
    print("Diámetro:", d)
elif teclado == 2:
    print("Perímetro:", p)
elif teclado == 3:
    print("Área:", a)
elif teclado == 4:
    print("Saliendo del programa")
else:
    print("Mensaje de error, debes volver a elegir")
