#from libreria24matematicas import sumarNumeros, restarNumeros, mostrarMenu
import libreria24matematicas

print("Calculadora métodos")

num1 = 0
num2 = 0
libreria24matematicas.mostrarMenu()
opcion = int(input())
resultado = 0
if(opcion == 1):
        resultado = libreria24matematicas.sumarNumeros(num1, num2)
elif(opcion == 2):
        resultado = libreria24matematicas.restarNumerosNumeros(num1, num2)
elif(opcion == 3):
        resultado = libreria24matematicas.multiplicarNumerosNumerosNumeros(num1, num2)
else:
        print("No ha seleccionado opción correcta")
print("Resultado:", resultado)
print("Fin de programa")