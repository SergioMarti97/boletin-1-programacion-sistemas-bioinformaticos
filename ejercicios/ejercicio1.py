# EJERCICIO 1
import bioinformatica as bio

print("==== EJERCICIO 1 ====")

genes = int(input("Introduce el número de genes: "))
bases = int(input("Introduce el número de bases: "))

print(f"Número de genes: {genes}\nNúmero de bases: {bases}\n"
      f"Promedio de bases por gen: {bio.average_genes(genes, bases)}")
