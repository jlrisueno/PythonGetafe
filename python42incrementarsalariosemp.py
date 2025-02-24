import oracledb

print("Incrementar salarios")

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

print("¿A qué oficio le incrementamos el salario?")
oficio = input()
print("¿Qué cantidad?")
cantidad = int(input())

sqlupdate = "update emp set salario=salario+:canti where oficio=:ofi"
cursor = connection.cursor()
cursor.execute(sqlupdate, (cantidad, oficio))
print("Empleados con incremento: " + str(cursor.rowcount))
cursor.close()

sqlselect = "select * from emp where oficio=:ofi"
cursor = connection.cursor()
cursor.execute(sqlselect, (oficio,))
for row in cursor:
    print("Apellido: "+row[1]+", Oficio: "+row[2]+", Salario: "+str(row[5]))
cursor.close()

connection.close()

print("Fin de programa")