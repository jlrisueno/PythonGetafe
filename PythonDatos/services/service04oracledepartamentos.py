import oracledb
from models import departamento

class ServiceOracleDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def insertarDepartamentos(self, numero, nombre, localidad):
        sql = "insert into dept values (:id, :nombre, :localidad)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def buscarDepartamento(self, numero):
        sql = "select * from dept where dept_no=:id"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero,))
        row = cursor.fetchone()
        modelo = departamento.Departamento()
        modelo.numero = row[0]
        modelo.nombre = row[1]
        modelo.localidad = row[2]
        cursor.close()
        return  modelo
    
    def eliminarDepartamento(self, numero):
        sql = "delete from dept where dept_no=:id"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero,))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros