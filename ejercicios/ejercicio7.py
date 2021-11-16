# EJERCICIO 7
import bioinformatica as bio

print("==== EJERCICIO 7 ====")

codon = input("Introduce un codon para traducir a aminoácido (solo 3 pares de bases): ")

print(f"Codon: {codon}\nAminoácido: {bio.translate_codon_case(codon)}")
