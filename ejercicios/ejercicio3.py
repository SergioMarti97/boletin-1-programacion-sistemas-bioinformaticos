# EJERCICIO 3
import bioinformatica as bio

print("==== EJERCICIO 3 ====")

dna = input("Introduce una secuencia de DNA: ")

print(f"DNA: {dna}\nRNA: {bio.replace_thymine_by_uracil(dna)}")
