import sys

text = sys.argv[1]


def num_vowels(text):
    vocal = ["a", "e", "i", "o", "u"]
    contador = 0
    for i in text.lower():
        if i in vocal:
            contador += 1
    return contador


def num_whitespaces(text):
    contador = 0
    for i in text:
        if i in " ":
            contador += 1
    return contador


def num_digits(text):
    contador = 0
    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in text:
        if i in digitos:
            contador += 1
    return contador


def num_words(text):
    palabras = text.split(" ")
    size = len(palabras)
    return size


def reverse(text):
    rever = text[-1::-1]
    return rever


def length(text):
    size_text = len(text)
    return size_text


def halfs(text):
    mitad = len(text) // 2
    primero = text[:mitad]
    segunda = text[mitad:]
    return primero, segunda


def upper_vowels(text):
    vocal = ["a", "e", "i", "o", "u"]
    enviar = ""
    for i in text:
        if i in vocal:
            enviar += i.upper()
        else:
            enviar += i
    return enviar


def sorted_by_words(text):
    ordenar = text.split()
    ordenar.sort()
    muestra = " ".join(ordenar)
    return muestra


def length_of_words(text):
    palabras = text.split()
    lista_palabras = list()
    for i in palabras:
        size = len(i)
        lista_palabras.append(str(size))
    muestra = " ".join(lista_palabras)
    return muestra


print("Number of vowels: ", num_vowels(text))
print("Number of whitespaces: ", num_whitespaces(text))
print("Number of digits: ", num_digits(text))
print("Number of words: ", num_words(text))
print("Reverse of text: ", reverse(text))
print("Length of text: ", length(text))
print("Halfs of text: ", (" | ". join(halfs(text))))
print("Text with uppercased vowels: ", upper_vowels(text))
print("Sorted by words: ", sorted_by_words(text))
print("Length of words: ", length_of_words(text))
