# Librería/módulo "bioinformatica.py"
import re


# Ejercicio 1
def average_genes(num_genes, num_bases):
    """
    (int, int) -> float
    Dado un número de genes y número de bases
    indica el número promedio de bases por gen

    :param num_genes: numero de genes
    :param num_bases: numero de bases
    :return: num_bases / num_genes

    >>> print(average_genes(120, 1400))
    """
    assert num_genes != 0
    return num_bases / num_genes


# Ejercicio 2
def concat_strings(string1, string2):
    """
    (string, string) -> string
    concatenar dos cadenas

    :param string1: cadena 1
    :param string2: cadena 2
    :return: cadena 1 concatenada con la cadena 2

    >>> print(concat_strings("Hola ", "mundo!"))
    """
    return string1 + string2


# Ejercicio 3
def replace_thymine_by_uracil(dna):
    """
    (string) -> string
    Substituir en una secuencia de DNA, las ocurrencias
    de T por ocurrencias de U (no utilizar la función replace)

    :param dna: la secuencia de DNA
    :return: la secuencia de DNA cambiando T por U (RNA)

    >>> dna = "ATGTCA"
    >>> rna = replace_thymine_by_uracil(dna)
    >>> print(f"DNA: {dna} RNA: {rna}")
    """
    rna = ""
    for i in range(0, len(dna)):

        if dna[i] == 'T':
            rna += 'U'
        else:
            rna += dna[i]

    return rna


# Ejercicio 4
def reverse_complement(dna):
    """
    (string) -> string
    Obtiene el complemento de la secuencia inversa
    de DNA (no usa los métodos translate ni maketrans)
    :param dna: la secuencia de DNA
    :return: la secuencia al revés y remplazando A por T, T por A, G por C y C por G

    >>> dna = "ATGCTA"
    >>> rc_dna = reverse_complement(dna)
    >>> print(f"DNA: {dna} reverse and complement: {rc_dna}")
    """
    result = ""
    for i in range(len(dna) - 1, -1, -1):
        if dna[i] == 'T':
            result += 'A'
        elif dna[i] == 'A':
            result += 'T'
        elif dna[i] == 'G':
            result += 'C'
        else:
            # dna[i] == 'C'
            result += 'G'

    return result


# Ejercicio 5:
def max_two_numbers(num1, num2):
    """
    (number, number) -> number
    Dado dos números, calcula el mayor

    :param num1: numero 1
    :param num2: numero 2
    :return: el mayor de los dos números

    >>> print(max_two_numbers(9, 8))
    """
    if num1 >= num2:
        return num1
    else:
        return num2


# Ejercicio 6:
def sort_three_numbers(num1, num2, num3):
    """
    (number, number, number) -> array(number)
    Dados tres eteros diferentes, ordénese de menor a mayor

    :param num1: numero 1
    :param num2: numero 2
    :param num3: numero 3
    :return: los tres números ordenados

    >>> a = 4
    >>> b = 3
    >>> c = 8
    >>> print(sort_three_numbers(a, b, c))
    """
    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp

    if num1 > num3:
        temp = num1
        num1 = num3
        num3 = temp

    if num2 > num3:
        temp = num2
        num2 = num3
        num3 = temp

    return [num1, num2, num3]


# Ejercicio 7:
def translate_codon_case(codon):
    """
    (string) -> character
    Traduce un codon a su aminoácido mediante un analisis de casos

    :param codon: secuencia de 3 bases nitrogenadas (ACGT)
    :return: un carácter indicando el aminoácido correspondiente

    >>> codon = "UGC"
    >>> print(f"codon: {codon} aminoácido: {translate_codon_case(codon)}")
    """
    if codon[0] == 'U':
        if codon[1] == 'U':
            if codon[2] == 'U':
                return 'F'  # Leucina
            elif codon[2] == 'C':
                return 'F'  # Leucina
            elif codon[2] == 'A':
                return 'L'  # Leucina
            else:
                return 'L'  # Leucina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return 'S'  # Serina
            elif codon[2] == 'C':
                return 'S'  # Serina
            elif codon[2] == 'A':
                return 'S'  # Serina
            else:
                return 'S'  # Serina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return 'Y'  # Tirosina
            elif codon[2] == 'C':
                return 'Y'  # Tirosina
            elif codon[2] == 'A':
                return '.'  # Stop
            else:
                return '.'  # Stop
        else:
            if codon[2] == 'U':
                return 'C'  # Cisteina
            elif codon[2] == 'C':
                return 'C'  # Cisteina
            elif codon[2] == 'A':
                return '.'  # Stop
            else:
                return 'W'  # Triptofano
    elif codon[0] == 'C':
        if codon[1] == 'U':
            if codon[2] == 'U':
                return 'L'  # Leucina
            elif codon[2] == 'C':
                return 'L'  # Leucina
            elif codon[2] == 'A':
                return 'L'  # Leucina
            else:
                return 'L'  # Leucina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return 'P'  # Prolina
            elif codon[2] == 'C':
                return 'P'  # Prolina
            elif codon[2] == 'A':
                return 'P'  # Prolina
            else:
                return 'P'  # Prolina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return 'H'  # Histidina
            elif codon[2] == 'C':
                return 'H'  # Histidina
            elif codon[2] == 'A':
                return 'Q'  # Glutamina
            else:
                return 'Q'  # Glutamina
        else:
            if codon[2] == 'U':
                return 'R'  # Arginina
            elif codon[2] == 'C':
                return 'R'  # Arginina
            elif codon[2] == 'A':
                return 'R'  # Arginina
            else:
                return 'R'  # Arginina
    elif codon[0] == 'A':
        if codon[1] == 'U':
            if codon[2] == 'U':
                return 'I'  # Isoleucina
            elif codon[2] == 'C':
                return 'I'  # Isoleucina
            elif codon[2] == 'A':
                return 'I'  # Isoleucina
            else:
                return '*'  # Metionina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return 'T'  # Treonina
            elif codon[2] == 'C':
                return 'T'  # Treonina
            elif codon[2] == 'A':
                return 'T'  # Treonina
            else:
                return 'T'  # Treonina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return 'N'  # Asparagina
            elif codon[2] == 'C':
                return 'N'  # Asparagina
            elif codon[2] == 'A':
                return 'K'  # Lisina
            else:
                return 'K'  # Lisina
        else:
            if codon[2] == 'U':
                return 'S'  # Serina
            elif codon[2] == 'C':
                return 'S'  # Serina
            elif codon[2] == 'A':
                return 'R'  # Arginina
            else:
                return 'R'  # Arginina
    else:
        # codon[0] == 'G'
        if codon[1] == 'U':
            if codon[2] == 'U':
                return 'V'  # Valina
            elif codon[2] == 'C':
                return 'V'  # Valina
            elif codon[2] == 'A':
                return 'V'  # Valina
            else:
                return 'V'  # Valina
        elif codon[1] == 'C':
            if codon[2] == 'U':
                return 'A'  # Alanina
            elif codon[2] == 'C':
                return 'A'  # Alanina
            elif codon[2] == 'A':
                return 'A'  # Alanina
            else:
                return 'A'  # Alanina
        elif codon[1] == 'A':
            if codon[2] == 'U':
                return 'D'  # Ac. aspartico
            elif codon[2] == 'C':
                return 'D'  # Ac. aspartico
            elif codon[2] == 'A':
                return 'E'  # Ac. glutamico
            else:
                return 'E'  # Ac. glutamico
        else:
            if codon[2] == 'U':
                return 'G'  # Glicina
            elif codon[2] == 'C':
                return 'G'  # Glicina
            elif codon[2] == 'A':
                return 'G'  # Glicina
            else:
                return 'G'  # Glicina


# Ejercicio 8:
def translate_codon_hash(codon):
    """
    (string) -> character
    Traduce un codon a su aminoácido mediante una tabla hash (diccionario)

    :param codon: secuencia de 3 bases nitrogenadas (ACTG)
    :return: un carácter indicando el aminoácido correspondiente

    >>> codon = "UGU"
    >>> print(f"codon: {codon} aminoácido: {translate_codon_hash(codon)}")
    """
    dic_translate = {
        "UUU": "F",  # 1
        "UUC": "F",  # 1

        "UUA": "L",  # 2
        "UUG": "L",  # 2
        "CUU": "L",  # 2
        "CUC": "L",  # 2
        "CUA": "L",  # 2
        "CUG": "L",  # 2

        "UCU": "S",  # 3
        "UCC": "S",  # 3
        "UCA": "S",  # 3
        "UCG": "S",  # 3
        "AGU": "S",  # 3
        "AGC": "S",  # 3

        "UAU": "Y",  # 4
        "UAC": "Y",  # 4

        "UAA": ".",  # 5 <- Stop
        "UAG": ".",  # 5 <- Stop
        "UGA": ".",  # 5 <- Stop

        "UGU": "C",  # 6
        "UGC": "C",  # 6

        "UGG": "W",  # 7

        "CCU": "P",  # 8
        "CCC": "P",  # 8
        "CCA": "P",  # 8
        "CCG": "P",  # 8

        "CAU": "H",  # 9
        "CAC": "H",  # 9

        "CAA": "Q",  # 10
        "CAG": "Q",  # 10

        "CGU": "R",  # 11
        "CGC": "R",  # 11
        "CGA": "R",  # 11
        "CGG": "R",  # 11
        "AGA": "R",  # 11
        "AGG": "R",  # 11

        "AUU": "I",  # 12
        "AUC": "I",  # 12
        "AUA": "I",  # 12

        "AUG": "*",  # 13 <- Start

        "ACU": "T",  # 14
        "ACC": "T",  # 14
        "ACA": "T",  # 14
        "ACG": "T",  # 14

        "AAU": "N",  # 15
        "AAC": "N",  # 15

        "AAA": "K",  # 16
        "AAG": "K",  # 16

        "GUU": "V",  # 17
        "GUC": "V",  # 17
        "GUA": "V",  # 17
        "GUG": "V",  # 17

        "GCU": "A",  # 18
        "GCC": "A",  # 18
        "GCA": "A",  # 18
        "GCG": "A",  # 18

        "GAU": "D",  # 19
        "GAC": "D",  # 19

        "GAA": "E",  # 20
        "GAG": "E",  # 20

        "GGU": "G",  # 21
        "GGC": "G",  # 21
        "GGA": "G",  # 21
        "GGG": "G"  # 21
    }

    return dic_translate.get(codon)


# Ejercicio 9:
def translate_codon_regex(codon):
    """
    (string) -> character
    Traduce un codon a su aminoácido mediante expresiones regex

    :param codon: secuencia de 3 bases nitrogenadas (ACTG)
    :return: un carácter indicando el aminoácido correspondiente

    >>> codon = "UGA"
    >>> print(f"codon: {codon} aminoácido: {translate_codon_regex(codon)}")
    """

    dic_translate_regex = {
        "UU[UC]": "F",  # 1
        "UU[AG]|CU.": "L",  # 2
        "UC.|AG[UC]": "S",  # 3
        "UA[UC]": "Y",  # 4
        "UA[AG]|UGA": ".",  # 5 <- Stop
        "UG[UC]": "C",  # 6
        "UGG": "W",  # 7

        "CC.": "P",  # 8
        "CA[UC]": "H",  # 9
        "CA[AG]": "Q",  # 10
        "CG.|AG[AG]": "R",  # 11

        "AU[UCA]": "I",  # 12
        "AUG": "*",  # 13 <- Start
        "AC.": "T",  # 14
        "AA[UC]": "N",  # 15
        "AA[AG]": "K",  # 16

        "GU.": "V",  # 17
        "GC.": "A",  # 18
        "GA[UC]": "D",  # 19
        "GA[AG]": "E",  # 20
        "GG.": "G"  # 21
    }

    for key in dic_translate_regex.keys():
        if re.match(key, codon):
            return dic_translate_regex.get(key)


# Ejercicio 10:
def distance_hamming(p, q):
    """
    (string, string) -> int

    Problema: DistanciaHamming(p, q)

    Calcula la distancia Hamming
    Se denomina distancia Hamming al número de discrepancias
    entre dos candeas p y q, siendo las dos cadenas del mismo
    tamaño k

    :param p: la cadena p
    :param q: la cadena q
    :return: la distancia hamming entre las dos cadenas

    >>> p = "ATGC"
    >>> q = "TTGC"
    >>> print(f"p: {p} q: {q} distance hamming between 'p' and 'q': {distance_hamming(p, q)}")
    """
    k = len(p)
    dist_hamming = 0
    for i in range(0, k):
        if p[i] != q[i]:
            dist_hamming += 1

    return dist_hamming


# Ejercicio 11:
# Parte A
def neighbours_dist1(seq):
    """
    (string) -> set(string)

    Problema: Vecinas1(patron)

    Encuentra las cadenas del mismo tamaño con una distancia
    hamming menor o igual que uno

    :param seq: la secuencia
    :return: un conjunto con todas las secuencias que tienen una distancia hamming menor o igual que uno con la
             secuencia original

    >>> seq = "ATGC"
    >>> print(neighbours_dist1(seq))
    """
    result = set()
    result.add(seq)
    bases = ['A', 'C', 'G', 'T']
    for i in range(0, len(seq)):
        neighbour = list(seq)
        for b in bases:
            if b != neighbour[i]:
                neighbour[i] = b
                result.add("".join(neighbour))

    return result


# Ejercicio 11:
# Parte B
def neighbours(seq, d):
    """
    (string, int) -> set(string)

    Problema: Vecinas(patron, d)

    Encuentra las cadenas del mismo tamaño, con una distancia
    hamming menor o igual que el valor de "d"

    :param seq: la secuencia
    :param d: la distancia hamming máxima
    :return: un conjunto con todas las secuencias quee tienen una distancia hamming menor o igual a la distancia "d"
             con la secuencia original

    >>> seq = "ATGC"
    >>> dist_hamming = 2
    >>> print(f"sequence: {seq}, distance hamming: {dist_hamming}, neigbours: ")
    >>> print(neighbours(seq, distance_hamming()))
    """
    result = set()
    result.add(seq)
    for i in range(0, d):
        temp = set()
        temp |= result
        for neighbour in temp:
            result |= neighbours_dist1(neighbour)

    return result


# Ejercicio 12:
# Parte A
def count_subsequence_in_sequence(mother, daughter):
    """
    (string, string) -> int

    Problema: Contar(texto, patron)

    Cuenta el número de apariciones de la cadena hija en la
    cadena madre. Tiene en cuenta solapamientos

    :param mother: cadena madre (grande)
    :param daughter: cadena hija o subsecuencia (pequeña)
    :return: el número de apariciones de la cadena hija en la cadena madre

    >>> m = "ATGCATGCATGCATGCATGC"
    >>> d = "AT"
    >>> print(f"mother: {m} daughter: {d} repetitions: {count_subsequence_in_sequence(m, d)}")
    """
    assert len(daughter) <= len(mother)
    end = len(mother) - len(daughter) + 1
    count = 0
    for i in range(0, end):
        if daughter == mother[i:i+len(daughter)]:
            count += 1

    return count


# Ejercicio 12:
# Parte B:
def count_most_repeat_kmeros(seq, k):
    """
    (string, int) -> list(string)

    Problema: PalabarasFrecuentes(texto, k)

    Calcula la subsecuencia de tamaño "k" que más se repite en la secuencia "seq"

    :param seq: la secuencia
    :param k: el tamaño de la subsecuencia, también llamado "kmero"
    :return: lista con los k-meros que más se repetien

    >>> m = "ATGCATGCATGCATGCATGC"
    >>> k = 4
    >>> print(f"sequence: {m} size of subsequence: {k} kmeros: ")
    >>> print(count_most_repeat_kmeros(seq, k))
    """

    assert k <= len(seq)
    kmeros = {}
    # Gracias a que tenemos la función que calcula el número de repeticiones
    # de una subcadena en una cadena grande, el mismo bucle que calcula el kmero
    # también puede contar el número de repeticiones del kmero en la secuencia grande
    for i in range(0, len(seq) - k + 1):
        kmero = seq[i:i+k]
        kmeros[kmero] = count_subsequence_in_sequence(seq, kmero)

    # Para ordenar utilizo la función sort y funciones lambda
    # Por defecto ordena de menor a mayor, con la función reverse obtengo el resultado que busco
    sorted_by_value = dict(reversed(sorted(kmeros.items(), key=lambda item: item[1])))
    # Filtro el diccionario para eliminar las entradas que solo tengan una repeticion
    max_repeats = list(sorted_by_value.values())[0]
    filtered_and_sorted = {k: v for k, v in sorted_by_value.items() if v > max_repeats}
    return filtered_and_sorted.keys()


# Ejercicio 13:
def search_pattern(pattern, text):
    """
    (string, string) -> list(int)

    Problema: BusquedaPatron(patron, texto)

    Encuentra la posición inicial para cada repeticion del patron en
    el texto

    :param pattern: el patron que se va a buscar en el texto
    :param text: el texto
    :return: una lista con las posiciones iniciales de cada repetición del patron

    >>> p = "ATG"
    >>> t = "ATGCTGTGAATTAA"
    >>> print(f"pattern: {p} text: {t} positions: ")
    >>> print(search_pattern(p, t))
    """
    assert len(pattern) <= len(text)
    end = len(text) - len(pattern) + 1
    first_appearances = []
    for i in range(0, end):
        if pattern == text[i:i + len(pattern)]:
            first_appearances.append(i)

    return first_appearances


# Ejercicio 14:
def aprox_search_pattern(pattern, text, dist_hamming):
    """
    (string, string) -> list(int)

    Problema: BusquedaAproximadaPatron(patron, texto, d)

    Encuentra las posiciones iniciales para cada repeticion del patron en
    el texto. Pero, se considera una ocurrencia entre patron y texto si la distancia
    Hamming entre ambas es menor o igual que un determinado valor

    :param pattern: el patron que se busca
    :param text: el texto donde se busca el patron
    :param dist_hamming: la distancia hamming con la que se calcula si existe ocurrencia o no
    :return: una lista con las posiciones iniciales para cada ocurrencia del patron en el texto

    >>> p = "ATG"
    >>> t = "ATGCTGTGAATTAA"
    >>> d = 2
    >>> print(f"pattern: {p} text: {t} distance hamming: {d} positions: ")
    >>> print(aprox_search_pattern(p, t, d))
    """
    assert len(pattern) <= len(text)
    end = len(text) - len(pattern) + 1
    first_appearances = []
    for i in range(0, end):
        if distance_hamming(pattern, text[i:i + len(pattern)]) <= dist_hamming:
            first_appearances.append(i)

    return first_appearances


# Ejercicio 15:
def most_repeat_word_with_discrepancies(text, k, d):
    """
    (string, int, int) -> list(string)

    Problema: PalabrasFrecuentesDiscrepancias(texto, k, d)

    Encontrar las palabras frecuentes en un texto con hasta un número
    máximo de discrepancias

    :param text: el texto
    :param k: el tamaño de los kmeros
    :param d: la distancia Hamming máxima
    :return: los kmeros o palabras más frecuentes de un texto, pero teniendo en cuenta discrepancias

    >>> t = "ATGCTGTGAATTAA"
    >>> k = 3
    >>> d = 2
    >>> print(f"text: {t} k: {k} d: {d} most repeat words: ")
    >>> print(most_repeat_word_with_discrepancies(t, k d))
    """
    # Nos aseguramos que k es menor o igual que la longitud total del texto
    assert k <= len(text)

    # Definimos un diccionario, key = kmero : value = ocurrencias aproximadas
    dic_kmeros_aprox = {}

    # Recorremos el texto, calculando los kmeros de tamaño k
    for i in range(0, len(text) - k + 1):
        kmero = text[i:i + k]
        # Para cada kmero, obtenemos sus "vecinos" con la distancia Hamming
        # que se pasa por parametro
        for kmero_aprox in neighbours(kmero, d):
            # Para cada vecino, calculamos el número de ocurrencias "similares"
            # usando la función que calcula la distancia hamming
            count = 0
            for j in range(0, len(text) - len(kmero_aprox) + 1):
                if distance_hamming(kmero_aprox, text[j:j + len(kmero_aprox)]) <= d:
                    count += 1
            # En el diccionario, guardamos el kmero aproximado y el número de
            # ocurrencias aproximadas
            dic_kmeros_aprox[kmero_aprox] = count

    # Para ordenar utilizo la función sort y funciones lambda
    # Por defecto ordena de menor a mayor, con la función reverse obtengo el resultado que busco
    sorted_by_value = dict(reversed(sorted(dic_kmeros_aprox.items(), key=lambda item: item[1])))
    # Filtro el diccionario para eliminar las entradas que solo tengan una repeticion
    max_repeats = list(sorted_by_value.values())[0]
    filtered_and_sorted = {k: v for k, v in sorted_by_value.items() if v >= max_repeats}
    return filtered_and_sorted.keys()
