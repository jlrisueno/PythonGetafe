import  oracledb

print("INSERTAR DOCTOR HOSPITAL")

connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
print("Introduzca apellido del doctor:")
apellido = input()
print("Introduzca especialidad:")
especialidad = input()
print("Introduzca salario:")
salario = input()

sqlhospitales = "select hospital_cod, nombre from hospital"
cursor = connection.cursor()
cursor.execute(sqlhospitales)
contador = 1
listahospitales = []
for hosp in cursor:
    print(f"{contador} - {hosp[1]}")
    listahospitales.append(hosp[0])
    contador = contador+1
cursor.close()
print("¿En qué hospital va a trabajar?")
opcion = int(input())
hospi = int(listahospitales[opcion-1])

sqlid = "select max(doctor_no)+1 from doctor"
cursor = connection.cursor()
cursor.execute(sqlid)
row = cursor.fetchone()
newid = row[0]
cursor.close()

sqlinsert = "insert into doctor values(:hos, :cod, :ape, :espe, :salar)"
cursor = connection.cursor()
cursor.execute(sqlinsert,(hospi, newid, apellido, especialidad, salario))
cursor.close()

cursor = connection.cursor()
sqlresult = "select * from doctor"
cursor.execute(sqlresult)
for row in cursor:
    print(row)
cursor.close()

connection.close()
print("Fin de programa")