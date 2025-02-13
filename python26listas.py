print("Listas con Python")
print("CREANDO LISTAS DE ENTEROS")
edades= [20,33,13,41,36,25]
print("Edad 1:",edades[0])
print("Edad 2:",edades[1])
# sort() ordena la lista de forma ASCENDENTE o alfabéticamente en texto
#edades.sort()
# de forma DESCENDENTE:
edades.sort(reverse = True)
for i in range(len(edades)):
    print(edades[i])
print("CREANDO LISTAS DE CADENAS")
nombre= ["Benito", "Javier", "Luis", "Laura", "Rosa", "Benito"]
print("Nombre 4:",nombre[3])
print("Nombre 3:",nombre[2])
print("Elementos en la lista nombres:",len(nombre))
# append() crea un elemento nuevo al final de la lista
nombre.append("Camela")
print("Nombre 6 (no existe):", nombre[6])
# insert() crea un elemento nuevo en la posición de la lista
nombre.insert(3, "José")
print("Nombre 4:",nombre[3])
# remove() elimina un objeto de la lista (si hay repetidos solo el 1º)
nombre.remove("Benito")
# pop() del() elimina un elemento por su posición
nombre.pop(4)
# del() también puede eliminar varios elementos
del nombre[0:2]
# clear() borra todo el contenido de una lista
#nombre.clear()
# Te indica con True o False si está en la lista un elemento
print("Camila" in nombre)
# Vamos a recorrer toda la lista y la mostramos
for i in range(len(nombre)):
    print(str(i), "=", nombre[i])
print(nombre)