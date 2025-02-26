from services import service04oracledepartamentos as ser
from models import departamento

print("--- SERVICIO ORACLE DEPARTAMENTOS ---")
servicio = ser.ServiceOracleDepartamentos()
print("1 - Insertar departamento")
print("2 - Buscar departamento")
print("3 - Eliminar departamento")
print("Seleccione una opción:")
opcion = int(input())
if (opcion == 1):
    print("Introduzca número de departamento:")
    num = int(input())
    print("Introduzca nombre:")
    nom = input()
    print("Introduzca localidad:")
    loc = input()
    afectados = servicio.insertarDepartamentos(num, nom, loc)
    print(f"Departamentos insertados: {afectados}")
elif (opcion == 2):
    print("Introduzca número de departamento:")
    num = int(input())
    dept = servicio.buscarDepartamento(num)
    print(f"{dept.numero} {dept.nombre} {dept.localidad}")
elif (opcion == 3):
    print("Introduzca número de departamento:")
    num = int(input())
    eliminados = servicio.eliminarDepartamento(num)
    print(f"Departamentos eliminados: {eliminados}")
else:
    print("Opción incorrecta")
print("FIN")