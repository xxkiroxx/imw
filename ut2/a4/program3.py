import sys

numero = int(sys.argv[1])
texto = sys.argv[2]
if numero > 0:
    palabras = texto.split(" ")
    size = len(palabras)
    contador = 0
    for i in range(0, size):
        if len(palabras[i]) == numero:
            contador += 1
    print(f"Hay {contador} palabras de tamaño {numero}")
else:
    print("El número introducido no es correcto")
