print("Rango de pares")
print("Introduce 1º número del rango")
primero = int(input())
print("Introduce 2º número del rango")
segundo = int(input())
print("Números pares:")
for i in range(primero, segundo):
    if(i%2==0):
        print(i)
print("Fin de programa")