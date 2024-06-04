# /*
#  * Crea una función que calcule el valor del parámetro perdido
#  * correspondiente a la ley de Ohm.
#  * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
#  *   el valor del tercero (redondeado a 2 decimales).
#  * - Si los parámetros son incorrectos o insuficientes, la función retornará
#  *   la cadena de texto "Invalid values".
#  */


def ohm_law(V=None, I=None, R=None):
    parametros = [V, I, R]
    f_param = [n for n in parametros if n is not None]
    if len(f_param) < 2:
        print("Invalid input, you must pass 2 arguments at least")
    if len(f_param) == 2:
        try:
            if V is None:
                V = round(I * R, 2)
                return V
            elif R is None:
                R = round(V / I, 2)
                return R
            elif I is None:
                I = round(V / R, 2)
                return I
        except (TypeError, ZeroDivisionError):
            return "Invalid values"
        
        
        
    if len(f_param) > 2:
        print("ERROR! More than 2 arguments was given")
        
    
ohm_law(V=5, I=2, R=1)
ohm_law(V=2, I=3)
print(ohm_law(V=4, R=112))
ohm_law(V=2)   