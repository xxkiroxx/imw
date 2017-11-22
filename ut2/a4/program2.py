import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100
sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])
a = 0
t = 0
g = 0
c = 0
for i in range(0, DNA_SIZE):
    if sequence[i] == "A":
        a += 1
    if sequence[i] == "T":
        t += 1
    if sequence[i] == "G":
        g += 1
    if sequence[i] == "C":
        c += 1
print(f" Adenine:{a}\n Thymine:{t}\n Cytosine:{c}\n Guanine:{g}")
