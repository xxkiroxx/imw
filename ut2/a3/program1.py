import sys

number = int(sys.argv[1])
if number <= 0:
    print("Este número no es valido.")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Es Divisible")
            break
    else:
        print("Es número primo")
