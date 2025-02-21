import oracledb

print("Introduzca turno de la plantilla (M T N):")
data = input()

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
sql = ("select apellido, funcion from plantilla where turno='" + data + "'")
cursor = connection.cursor()
cursor.execute(sql)

for row in cursor:
    print("Apellido: "+ row[0] +" - Función: "+ row[1])

cursor.close()
connection.close()

print("Fin de programa")