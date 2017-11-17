import sys

number = int(sys.argv[1])
if number < 0:
    print(" Error el número no es positivo")
else:
    for i in range(1, number + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        print(i, "!=", factorial)
