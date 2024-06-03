# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def prime(a):
    is_prime = True
    for n in range(2, a//2 + 1 ):
        if a % n == 0:
            is_prime = False
    return is_prime

for n in range(100,201):
    print(f"{n} = {prime(n)}")
            
        
    