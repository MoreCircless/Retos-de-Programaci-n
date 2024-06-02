import math
# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */


numero_dec = input("Que numero quiere cambiar de base decimal a base binaria?")
numero_decimal = int(numero_dec)
numero = []
def dec_a_bin(num: int):
    if num == 1:
        numero.append(int(1))
    elif num == 0:
        numero.append(int(0))
    else:
        variable = int(num) % 2 
        numero.append(int(variable))
        nuevo_num = num / 2
        numero_floor = math.floor(nuevo_num)
        dec_a_bin(int(numero_floor))
        



print("El número binario es:", "".join(map(str, numero[::-1])))
