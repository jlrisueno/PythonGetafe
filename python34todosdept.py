import oracledb

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
sql = "select * from dept"
cursor = connection.cursor()
cursor.execute(sql)

for row in cursor:
    print(row)
    #fila
    # print(row[0])
    # print(row[1])
    # print(row[2])
    #columna NO funciona en ORACLE
    # nombre = row.dnombre
    # print(nombre)

#el cursor solo se puede leer una vez. Si quieremos volver a leer hay que ejecutar de nuevo execute()
cursor.execute(sql)

for numero, nombre, localidad in cursor:
    print(str(numero), " ", nombre, " ", localidad)

cursor.close()
connection.close()

print("Fin de programa")