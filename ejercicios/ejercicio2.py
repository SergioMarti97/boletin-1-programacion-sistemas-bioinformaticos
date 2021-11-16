# EJERCICIO 2
import bioinformatica as bio

print("==== EJERCICIO 2 ====")

str1 = input("Introduce una cadena: ")
str2 = input("Introduce otra cadena: ")

print(f"Cadena 1: {str1}\nCadena 2: {str2}\nLas dos cadenas concatenadas: {bio.concat_strings(str1, str2)}")
