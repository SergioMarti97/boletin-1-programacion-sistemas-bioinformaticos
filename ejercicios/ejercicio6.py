# EJERCICIO 6
import bioinformatica as bio

print("==== EJERCICIO 6 ====")

num1 = int(input("Introduce el número 1: "))
num2 = int(input("Introduce el número 2: "))
num3 = int(input("Introduce el número 3: "))

print(f"Número 1: {num1}\nNúmero 2: {num2}\nNúmero 3: {num3}\nOrdenados: {bio.sort_three_numbers(num1, num2, num3)}")
