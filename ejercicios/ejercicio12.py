# EJERCICIO 12

import bioinformatica as bio

print("==== EJERCICIO 12 ====")

mother = input("Introduce una secuencia de DNA: ")
size_kmero = int(input("Introduce el tamaño de la subsecuencia: "))
kmeros = bio.count_most_repeat_kmeros(mother, size_kmero)

print(f"Secuencia: {mother}\nkmeros: {kmeros}")
