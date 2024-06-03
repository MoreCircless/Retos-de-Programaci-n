# /*
#  * Escribe una función que reciba un texto y retorne verdadero o
#  * falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee
#   * de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.
#  */


def palindromo(text: str) -> bool:
    inv_text = text[::-1]
    if inv_text == text:
        return True
    else:
        return False
    
    

user_input = input("Que texto quieres comprobar?\n-> ").lower()

print(palindromo(user_input.replace(" ", "")))