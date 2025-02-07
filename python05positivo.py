print("Número positivo, negativo o cero.")
print("Introduzca un número:")
numero = int(input())
if(numero > 0):
    print("POSITIVO")
else:
    if(numero == 0):
        print("CERO")
    else:
        print("NEGATIVO")
print("Fin del programa.")

print("Otra opción más correcta con elif")
if(numero > 0):
    print("POSITIVO")
elif(numero == 0):
    print("CERO")
else:
    print("NEGATIVO")
print("Fin del programa elif.")