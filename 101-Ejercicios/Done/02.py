# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */


def anagrama(palabra_1, palabra_2):
    if palabra_1 == palabra_2 or len(palabra_1) != len(palabra_2):
        return False
    else:
        format_palabra_1 = list(palabra_1.lower()).sort()
        format_palabra_2 = list(palabra_2.lower()).sort()
        if format_palabra_1 == format_palabra_2:
            return True
        else:
            return False



palabra_1 = input("Palabra 1: ")
palabra_2 = input("Palabra 2: ")

print(anagrama(palabra_1, palabra_2))