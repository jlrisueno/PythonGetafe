import oracledb

print("Introduzca inscripción de enfermo:")
data = input()

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
sql = "select apellido, direccion from enfermo where inscripcion=" + data
cursor = connection.cursor()
cursor.execute(sql)

row = cursor.fetchone()

# comprobamos si la fila tiene contenido:
if (not row):
    print("No existe el enfermo.")
else:
    print(row)

cursor.close()
connection.close()

print("Fin de programa")