print("Métodos string")
texto = "primero python"
print("upper ", texto.upper())
print("replace " + texto.replace("o", "@"))
print("count letra o:", texto.count("o"))
print("Letra 0: " + texto[0])
print("Longitud (len)", len(texto))
print("find letra P: ", texto.find("p"))
print("rfind letra P: ", texto.rfind("p"))
print("find letra Z (no existe): ", texto.find("z"))
print("find letra P sobrecarga pos 0: ", texto.find("p",0))
print("find letra P sobrecarga pos 1: ", texto.find("p",1))
print("startswith letra A: ", texto.startswith("A"))
print("startswith letra p: ", texto.startswith("p"))
print("endswith letra N (mayuscula):", texto.endswith("N"))
print("isdigit()", texto.isdigit())
print("isalpha()", texto.isalpha())
print("isalnum()", texto.isalnum())
print("isalpha y isalnum dan False por el ESPACIO")
substring = texto[2:]
print("Posición 2 en adelante: ", substring)
subtexto = texto[2:5]
print("Posición 2 a la 5: ", subtexto)
longitud = len(texto)
for i in range(longitud):
    letra = texto[i]
    print("Posición", i ,":", letra)
print("Comprobación de que se introduce un número:")
print("Introduzca un número:")
aux = input()
print(aux.isdigit())
if(aux.isdigit()):
    print("Esto es un número! :)")
else:
    print("No es un número...")
print("Fin de programa")