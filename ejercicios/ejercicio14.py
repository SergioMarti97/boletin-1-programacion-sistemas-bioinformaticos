# EJERCICIO 14

import bioinformatica as bio

print("==== EJERCICIO 14 ====")

text = input("Introduce una texto: ")
pattern = input("Introduce un patron a buscar en el texto (se buscará de forma aproximada): ")
first_appearances = bio.aprox_search_pattern(pattern, text, 1)

print(f"Posición donde coincide de forma aproximada el patron con el texto: {first_appearances}")