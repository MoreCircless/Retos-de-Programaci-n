# /*
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  */


cadena_usuario = input("Que desea invertir?\n-> ")

nueva_cadena = cadena_usuario[::-1]

print(nueva_cadena)