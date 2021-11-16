# EJERCICIO 10
import bioinformatica as bio

print("==== EJERCICIO 10 ====")

str1 = input("Introduce una cadena de DNA: ")
str2 = input("Introduce otra cadena de DNA: ")
dist_haming = bio.distance_hamming(str1, str2)

print(f"Cadena 1: {str1}\nCadena 2: {str2}\nDistancia Hamming: {dist_haming}")
