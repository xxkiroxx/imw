import sys

dni = int(sys.argv[1])
cadena = "TRWAGMYFPDXBNJZSQVHLCKE"
calculo = dni % 23
letra = cadena[calculo]
print(f"Mi dni es {dni}-{letra}")
