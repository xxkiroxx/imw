import sys

# Por comando debe escribir los números
number1 = int(sys.argv[1])
number2 = int(sys.argv[2])
mcd = False
if number1 > 0 and number2 > 0 and number1 != number2:
    if number2 < number1:
        number1, number2 = number2, number1
    i = number1
    while not mcd and i >= 1:
        if number1 % i == 0 and number2 % i == 0:
            print("El máximo común divisor es", i)
            mcd = True
        else:
            i -= 1
else:
    if number1 <= 0 or number2 <= 0:
        print("Los números introducidos son incorrectos")
    else:
        print("Los números son iguales")
