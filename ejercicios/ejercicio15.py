# EJERCICIO 15

import bioinformatica as bio

print("==== EJERCICIO 15 ====")

seq = input("Introduce una secuencia de DNA: ")
size_kmero = int(input("Introduce el tamaño de la subsecuencia: "))
dist_hamming = int(input("Introduce una distancia Hamming: "))
kmeros_aprox = bio.most_repeat_word_with_discrepancies(seq, size_kmero, dist_hamming)

print(f"Secuencia: {seq}\nTamaño de los kmeros: {size_kmero}\nDistancia Hamming: {dist_hamming}\n"
      f"kmeros aproximados: {kmeros_aprox}")

