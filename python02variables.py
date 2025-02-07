print("Ejemplo variable")
#ESTO ES UN COMETARIO.
#COMENTAR: COMAND + K + C
#DESCOMENTAR: COMAND + K + U
#Las variables no tienen tipo, éstas se escriben en minuscula.
numero = 13
texto = "Variables de tipo String"
print(numero)
print(texto)
print("Concatenación:", numero, "+", texto)
print("Otra opción:" + str(numero) + "+" + texto)
#Al usar + en una variable de tipo número está intentando hacer una suma, entonces antes hay que transformarla a string.
# str(variable): convierte una variable a string.
# float(variable): convierte una variable a decimal.
# int(variable): convierte una variable a número entero.
textonumero = "123"
minumero = int(textonumero)
suma = minumero + numero
print(suma)
print(minumero / numero)