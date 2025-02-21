import oracledb

# conectar a la base de datos
connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

# consulta sql
sql = "select * from dept"

# crear y ejecutar el cursor
cursor = connection.cursor()
cursor.execute(sql)

# con fetchone() avanza fila a fila
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)
row = cursor.fetchone()
print(row)

# cerrar conexiones
cursor.close()
connection.close()
print("Fin de programa!!!")