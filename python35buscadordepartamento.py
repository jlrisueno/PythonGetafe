import oracledb

print("Introduzca número de departamento:")
data = input()

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
sql = "select * from dept where dept_no=" + data
cursor = connection.cursor()
cursor.execute(sql)

row = cursor.fetchone()

# comprobamos si la fila tiene contenido:
if (not row):
    print("No existe el departamento.")
else:
    print(row)

cursor.close()
connection.close()

print("Fin de programa")