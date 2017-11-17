import sys

number = int(sys.argv[1])
suma = 0
if number < 0:
    print("El número es negativo", number)
else:
    for i in range(1, number + 1):
        suma = suma + (i ** 2)
# alias suma += i ** 2
    print("Número de entrada=", number)
    print("Salida=", suma)
