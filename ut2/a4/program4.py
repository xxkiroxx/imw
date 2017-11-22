import sys

cadena = sys.argv[1:]
contar = len(cadena)
contador = 0
for i in cadena:
    i = float(i)
    contador += i
resultado = contador / contar
print(f"La media entre los números es {resultado}")
