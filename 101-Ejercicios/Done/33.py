# /*
#  * Dado un listado de números, encuentra el SEGUNDO más grande
#  */


def second_higher(lista: list) -> int:
    new_list = lista
    higher = 0
    sec_higher = 0
    for num in new_list:
        if num > higher:
            higher = num
    new_list.remove(higher)
    for num in new_list:
        if num > sec_higher:
            sec_higher = num
            
    return sec_higher


lista = [1, 2, 3, 4, 5, 67, 24224, 2, 4]
print(second_higher(lista=lista))