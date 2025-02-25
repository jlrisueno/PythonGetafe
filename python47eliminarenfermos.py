from conexionoracle47eliminarenfermos import ConexionOracleEnfermos

print("Probando clases de Oracle: ENFERMOS")
print("1.- Eliminar")
print("2.- Modificar apellido")
print("Seleccione una opción")
opcion = int(input())
print("Introduzca una inscripción:")
inscripcion = int(input())
connection = ConexionOracleEnfermos()
if (opcion == 1):
    eliminados = connection.eliminarEnfermo(inscripcion)
    print(f"Enfermos eliminados: {eliminados}")
elif (opcion == 2):
    print("Introduzca nuevo apellido:")
    apellido = input()
    modificar = connection.modificarEnfermo(apellido, inscripcion)
    print(f"Enfermos modificados: {modificar}")
else:
    print("Opción incorrecta.")
print("Fin de programa")