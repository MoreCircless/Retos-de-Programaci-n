# /*
#  * Crea una función que reciba días, horas, minutos y segundos (como enteros)
#  * y retorne su resultado en milisegundos.
#  */

dias = int(input("Dias -> "))
horas = int(input("Horas -> "))
minutos = int(input("Minutos -> "))
segundos = int(input("Segundos -> "))

# Primero voy a pasar todos los datos a segundos, despues lo pasare a milisegundos
def time_to_ms(dias, horas, minutos, segundos):
    recuento = 0
    recuento += (dias * 60 * 60 * 24) + (horas * 60 * 60) + (minutos * 60) + segundos
    recuento = recuento * 1000
    return recuento 


print(time_to_ms(dias, horas, minutos, segundos))
