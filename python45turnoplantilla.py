import  oracledb

print("TURNOS PLANTILLA")

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
sqlturno = "select DISTINCT turno from plantilla"
cursor = connection.cursor()
cursor.execute(sqlturno)
contador = 1
listaturnos = []
for turno in cursor:
    print(f"{contador} - {turno[0]}")
    listaturnos.append(turno[0])
    contador = contador+1
cursor.close()
print("Selecciona una opción:")
opcion = int(input())
turno = listaturnos[opcion-1]

cursor = connection.cursor()
sqlplantilla = "select * from plantilla where turno=:p1"
cursor.execute(sqlplantilla, (turno, ))
for row in cursor:
    print(row)
cursor.close()

connection.close()
print("Fin de programa")