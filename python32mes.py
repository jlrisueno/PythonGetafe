from class32mes import Mes
import random

print("Ejemplo clase mes")
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
for nombreMes in meses:
    mes = Mes()
    mes.nombre = nombreMes
    mes.tempMaxima = random.randint(1,40)
    mes.tempMinima = random.randint(1,40)
    print(mes)
    print("Media de", mes.getTemperaturaMedia())
# mes2 = Mes()
# mes2.nombre = "Febrero"
# mes2.tempMaxima = 25
# mes2.tempMinima = 10
# print(mes2)
# print("Media de", mes2.getTemperaturaMedia())
print("Fin de programa")