import oracledb

print("Incrementar salario plantilla")

print("Introduce el código del hospital:")
codigo = int(input())
print("Introduce el incremento:")
incre = int(input())

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
cursor = connection.cursor()
sqlupdate = "update plantilla set salario=salario+:sal where hospital_cod=:cod"
cursor.execute(sqlupdate, (incre, codigo))
print(f"Modificados: {str(cursor.rowcount)}")
cursor.close()

cursor = connection.cursor()
sql = "select apellido, funcion, salario from plantilla where hospital_cod=:cod"
cursor.execute(sql, (codigo,))
for ape, fun, sal in cursor:
    print(f"Apellido {ape}, función {fun}, salario {sal}")
cursor.close()

connection.close()
print("Fin de programa")