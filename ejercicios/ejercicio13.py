# EJERCICIO 13

import bioinformatica as bio

print("==== EJERCICIO 13 ====")

text = input("Introduce una texto: ")
pattern = input("Introduce un patron a buscar en el texto: ")
first_appearances = bio.search_pattern(pattern, text)

print(f"Posición donde coincide el patron con el texto: {first_appearances}")
