# /*
#  * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
#  * - Recuerda que todas las instrucciones de participación están en el
#  *   repositorio de GitHub.
#  *
#  * Lo primero... ¿Ya has elegido un lenguaje?
#  * - No todos son iguales, pero sus fundamentos suelen ser comunes.
#  * - Este primer reto te servirá para familiarizarte con la forma de participar
#  *   enviando tus propias soluciones.
#  *
#  * EJERCICIO:
#  * - Crea un comentario en el código y coloca la URL del sitio web oficial del
#  *   lenguaje de programación que has seleccionado.
#  * - Representa las diferentes sintaxis que existen de crear comentarios
#  *   en el lenguaje (en una línea, varias...).
#  * - Crea una variable (y una constante si el lenguaje lo soporta).
#  * - Crea variables representando todos los tipos de datos primitivos
#  *   del lenguaje (cadenas de texto, enteros, booleanos...).
#  * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
#  *
#  * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
#  * debemos comenzar por el principio.
#  */




# Esto es un comentario
# https://python.org

"""
Esto tambien es un comentario 
pero en 
varias
lineas
"""

'''
Esto tambien es un comentario 
pero 
de diferente forma
'''

mi_variable = 12
mi_variable = "hola mundo"

# EN PYTHON NO EXISTEN LAS CONSTANTES, ESTAS POR CONVENCION SE ESTABLECEN
# PONIENDO EL NOMBRE DE LA VARIABLE EN MAYUSCULA 

MI_CONSTANTE = "Mi constante" # por convencion es una constante, pero proceduralmente puede variar

#  TIPO: Entero "int"
my_int_1: int = 1
my_int_2 = 2

print(type(my_int_1))

#  TIPO: Coma flotante "float"
my_float_1: float = 3.04
my_float_2 = 4.50432

print(type(my_float_1))

# Tipo: Booleano "bool"
my_boal_1: bool = False
my_boal_2 = False

print(type(my_boal_1))

# Tipo: String, o cadena de texto "str"
my_str_1: str = "Hola mundo, esto es una string"
my_str_2 = 'ESto tambien es una string, pero con otras comillas'

print(type(my_str_1))


print("¡Hola, Python!")








