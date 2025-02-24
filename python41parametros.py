import oracledb

print("Ejemplo de parámetros Oracle")

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("Introduzca número del departamento:")
iddept = int(input())

# con "f" antes de un stream "" podemos poner variables dentro de "{}"" sin concatenarlas
#sql = f"select * from emp where dept_no={iddept}"
# depués de los ":" envíamo los parámetros en el execute del sql
# hay que usar esa forma porque nos pueden meter código a traves del formulario (inyección sql)
sql = "select * from emp where dept_no=:parametros"
print(sql)
cursor = connection.cursor()
cursor.execute(sql, (iddept,))
for row in cursor:
    print(f"Apellido: {row[1]}, oficio: {row[2]}, departamento: {row[7]}")
cursor.close()

connection.close()

print("Fin de programa")