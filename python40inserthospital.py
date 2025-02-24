import oracledb

print("Insertar hospital")

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca código del hospital:")
codhospi = input()
print("Introduzca nombre:")
nombre = input()
print("Introduzca dirección:")
dire = input()
print("Introduzca tlf:")
tlf = input()
print("Introduzca número de camas:")
camas = input()

sqlinsert = "insert into hospital values(" + codhospi + ",'" + nombre + "','" + dire + "','" + tlf + "'," + camas + ")"
cursor = connection.cursor()
cursor.execute(sqlinsert)
print("Hospitales insertados: " + str(cursor.rowcount))
cursor.close()

sqlselect = "select * from hospital"
cursor = connection.cursor()
cursor.execute(sqlselect)
for row in cursor:
    print(row)
cursor.close()

connection.close()

print("Fin de programa")