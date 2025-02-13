import libreria25validaciones

def mostrarMenu():
    print("Seleccione una opción:")
    print("1.- Validar ISBN")
    print("2.- Mostrar letra DNI")

print("Método validaciones")

mostrarMenu()
opcion = int(input())
resultado = 0
isbn = 0
dni = 0
if(opcion == 1):
        # 8441513929
        print("Introduce número ISBN:")
        isbn = input()
        resultado = libreria25validaciones.validarISBN(isbn)
elif(opcion == 2):
        print("Introduce número de DNI:")
        dni = int(input())
        resultado = libreria25validaciones.letraDNI(dni)
else:
        print("No ha seleccionado opción correcta")
print("Resultado:", resultado)
print("Fin de programa")