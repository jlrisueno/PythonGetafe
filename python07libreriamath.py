#LIBRERIAS: una funcionalidad con una serie de características, son metodos especializados en algo que estan por defecto en nuestro programa.
#Tenemos algunas que están nativas en Python y otras las tenemos que instalar.
print("Ejemplo de librerías.")
#Sintaxis con from:
from math import floor, ceil, trunc
#Sintaxis con import:
#import math
#varFloor = math.floor(division)
numero1 = 20
numero2 = 3
division = numero1 / numero2
print("La división es: ", division)
#Declaramos variables para almacenar los valores:
varFloor = floor(division)
varCeil = ceil(division)
varTrunc = trunc(division)
print("Floor:", varFloor)
print("Ceil:", varCeil)
print("Trunc:", varTrunc)
print("Fin de programa.")