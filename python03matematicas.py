print("Ejemplo mates variables")
numero1 = 20
numero2 = 3
print("Números:", numero1, " y ", numero2)
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
redondeo = int(division)
print("División sin decimales:", redondeo)
print(str(numero1) + " * " + str(numero2)+ " = " + str(multiplicacion))

#Cuando pidamos valores al usuario siempre seran de tipo string.
print("Introduzca el valor de número 3:")
numero3 = input()
print("Introduzca el valor de número 4:")
numero4 = input()
print(numero3, numero4)
print("Sin transformar a int: ", numero3 + numero4)
print("Transformando a int: ", numero3, " + ", numero4, " = ", int(numero3) + int(numero4))