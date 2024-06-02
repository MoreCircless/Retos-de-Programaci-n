# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */





def poligono(b, t, h=1):
    area = b * h
    if t.lower() == "t":
        return area / 2
    elif t.lower() == "c":
        return b**2
    else:
        return area


tipo = input("Elige (T)riangulo, (C)uadrado o (R)ectangulo")
base = int(input("Que base tiene? -> "))
altura = 1
if tipo.lower() != "c":
    altura = int(input("Que altura tiene? -> "))
print(poligono(base, tipo, altura))
    
    
