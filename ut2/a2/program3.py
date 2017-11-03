
import sys

nota = float(sys.argv[1])

if nota < 5:
    print("Suspenso")
elif 5 <= nota < 7:
    print("Aprobando")
elif 7 <= nota < 9:
    print("Notable")
elif 9 <= nota < 10:
    print("Sobresaliente")
else:
    print("Matrícula de honor")
