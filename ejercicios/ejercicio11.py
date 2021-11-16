# EJERCICIO 11

import bioinformatica as bio

print("==== EJERCICIO 11 ====")

seq = input("Introduce un patron de DNA: ")
d = int(input("Introduce una distancia Hammming: "))

print(f"Vecinas:\n{bio.neighbours(seq, d)}")
