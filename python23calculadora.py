def mostrarMenu():
    print("Seleccione una opción:")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Introducir otros números")
    print("0.- Salir")

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def intronum():
    num1 = ""
    num2 = ""
    while(num1.isdigit()==False):
        print("Introduzca primer número")
        num1 = input()
    num1 = int(num1)
    while(num2.isdigit()==False):
        print("Introduzca segundo número")
        num2 = input()
    num2 = int(num2)
    mostrarMenu()
    return num1, num2

print("Calculadora")
num = intronum()
num1 = num[0]
num2 = num[1]
#mostrarMenu()
#opcion = int(input())
#resultado = ""
#if(opcion == 1):
#    resultado = sumar(num1, num2)
#elif(opcion == 2):
#    resultado = restar(num1, num2)
#elif(opcion == 3):
#    resultado = multiplicar(num1, num2)
#else:
#    print("Opción no encontrada")
#print("Resultado:",resultado)
opcion = -1
while(opcion!=0):
    if(opcion !=-1):
        mostrarMenu()
    opcion = int(input())
    resultado = ""
    if(opcion == 1):
        resultado = sumar(num1, num2)
    elif(opcion == 2):
        resultado = restar(num1, num2)
    elif(opcion == 3):
        resultado = multiplicar(num1, num2)
    elif(opcion == 4):
        num = intronum()
        num1 = num[0]
        num2 = num[1]
    elif(opcion == 0):
        print("Buen día")
    else:
        print("Opción no encontrada")
    if(opcion != 0):
        print("Resultado:",resultado)
print("Fin de programa")