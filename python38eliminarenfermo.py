import oracledb

print("Introduzca inscripción del enfermo a eliminar:")
data = input()

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
sql = "delete from enfermo where inscripcion=" + data
cursor = connection.cursor()
cursor.execute(sql)

# rowcount: devulve el INT de la acción
afectados = cursor.rowcount
connection.commit()
print("Registros eliminados: " + str(afectados))
cursor.close()

sqlselect = "select * from enfermo"
cursor = connection.cursor()
cursor.execute(sqlselect)
print("------ ENFERMOS ------")
for row in cursor:
        print("Inscripción: " + str(row[0]) + " - " + row[1])
cursor.close()

connection.close()
print("Fin de programa")