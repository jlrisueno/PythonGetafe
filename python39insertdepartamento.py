import oracledb

print("Insertar departamentos")

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca un ID de departamento:")
iddept = input()
print("Introduzca nombre:")
nombre = input()
print("Introduzca localidad:")
localidad = input()

sqlinsert = "insert into dept values(" + iddept + ",'" + nombre + "','" + localidad + "')"
cursor = connection.cursor()
cursor.execute(sqlinsert)
print("Departamentos insertados: " + str(cursor.rowcount))
cursor.close()

sqlselect = "select * from dept"
cursor = connection.cursor()
cursor.execute(sqlselect)
for row in cursor:
    print(row)
cursor.close()

connection.close()

print("Fin de programa")