# EJERCICIO 9
import bioinformatica as bio

print("==== EJERCICIO 9 ====")

codon = input("Introduce un codon para traducir a aminoácido (solo 3 pares de bases): ")

print(f"Codon: {codon}\nAminoácido: {bio.translate_codon_regex(codon)}")
