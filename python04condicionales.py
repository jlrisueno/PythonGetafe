#Una condicional es una pregunta dentro del código.
#Para aplicar los condicionales en Python tenemos que aplicar tabulaciones.
# == igual
# != distinto

print("¿Es mayor de edad?")
edad = 18
if(edad >= 18):
    print("Es mayor de edad")
    print("Seguimos dentro del IF")
print("Fin del programa")

print("Condicional número 1:")
numero1 = input()
print("Condicional número 2:")
numero2 = input()
print(numero1, numero2)
if(int(numero1) > int(numero2)):
    print("Numero 1 es MAYOR que 2")
else:
    print("Numero 1 es MENOR que 2")