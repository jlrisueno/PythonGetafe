def mostrarMenu():
    print("Seleccione una opción:")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

def restar(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

print("Calculadora")
print("Introduzca primer número")
num1 = int(input())
print("Introduzca segundo número")
num2 = int(input())
mostrarMenu()
opcion = int(input())
resultado = ""
if(opcion == 1):
    resultado = sumar(num1, num2)
elif(opcion == 2):
    resultado = restar(num1, num2)
elif(opcion == 3):
    resultado = multiplicar(num1, num2)
else:
    print("Opción no encontrada")
print("Resultado:",resultado)
print("Fin de programa")