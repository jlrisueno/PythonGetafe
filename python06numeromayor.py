print("NÚMERO MAYOR, MENOR O IGUAL")

print("Número 1:")
numero1 = int(input())
print("Número 2:")
numero2 = int(input())

if(numero1 == numero2):
    print(str(numero1) + " y " + str(numero2) + " son iguales.")
elif(numero1 > numero2):
    print("Numero 1 es MAYOR que 2")
else:
    print("Numero 1 es MENOR que 2")