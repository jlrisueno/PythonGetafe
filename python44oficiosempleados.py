import  oracledb

print("OFICIOS EMPLEADOS")

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
sqloficio = "select DISTINCT oficio from emp"
cursor = connection.cursor()
cursor.execute(sqloficio)
contador = 1
listaoficio = []
for ofi in cursor:
    print(f"{contador} - {ofi[0]}")
    listaoficio.append(ofi[0])
    contador = contador+1
cursor.close()
print("Selecciona una opción:")
opcion = int(input())
oficio = listaoficio[opcion-1]

cursor = connection.cursor()
sqlempleados = "select * from emp where oficio=:p1"
cursor.execute(sqlempleados, (oficio, ))
for row in cursor:
    print(row)
cursor.close()

connection.close()
print("Fin de programa")