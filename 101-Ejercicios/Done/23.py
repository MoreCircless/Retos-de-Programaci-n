# /*
#  * Crea una función que reciba dos array, un booleano y retorne un array.
#  * - Si el booleano es verdadero buscará y retornará los elementos comunes
#  *   de los dos array.
#  * - Si el booleano es falso buscará y retornará los elementos no comunes
#  *   de los dos array.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.
#  */

def conjuntos(list1: list, list2: list, boolean: bool) -> list:
    if boolean:
        return_list = [a for a in list1 if a in list2]
        return return_list
    else:
        return_list = [a for a in list1 if a in list2]
        f_list1 = [a for a in list1 if a not in return_list]
        f_list2 = [a for a in list2 if a not in return_list]
        f_list1.extend(f_list2)
        return f_list1
    
    
    

lista1 = [1, 3, 5, 8, 10 ]
lista2 = [2, 4, 5, 7, 10]


print(conjuntos(list1=lista1, list2=lista2, boolean=True))
print(conjuntos(list1=lista1, list2=lista2, boolean=False))