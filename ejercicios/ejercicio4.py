# EJERCICIO 4
import bioinformatica as bio

print("==== EJERCICIO 4 ====")

dna = input("Introduce una secuencia de DNA: ")

print(f"--- DNA ---\n{dna}\n--- Reversa y Complementaria ---\n{bio.reverse_complement(dna)}")
