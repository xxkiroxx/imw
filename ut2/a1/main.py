import sys


caja = int(sys.argv[1])

# Variables de Billetes

cincuenta = 50
veinte = 20
diez = 10
cinco = 5

# Variables de Monedas

dos = 2
uno = 1

if caja // cincuenta >= 1:
    print (caja // cincuenta, "Billete/s de 50€  ")
    caja = caja % cincuenta
if caja // veinte >= 1:
    print (caja // veinte, "Billete/s de 20€ ")
    caja = caja % veinte
if caja // diez >= 1:
    print (caja // diez, "Billete/s de 10€ ")
    caja = caja % diez
if caja // cinco >= 1:
    print (caja // cinco, "Billete/s de 5€ ")
    caja = caja % cinco
if caja // dos >= 1:
    print (caja // dos, "Moneda/s de 2€ ")
    caja = caja % dos
if caja // uno >= 1:
    print (caja // uno, "Moneda/s de 1€ ")
    caja = caja % uno