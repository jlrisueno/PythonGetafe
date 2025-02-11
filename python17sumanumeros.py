print("Ejercicio suma números.")
print("Introduce un número en texto:")
texto = input()
resultado = 0
for i in range(len(texto)):
    resultado = resultado + int(texto[i])
print("Suma texto:", resultado)