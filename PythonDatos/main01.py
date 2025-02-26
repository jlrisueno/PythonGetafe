from services import service01prueba as ser
from models import mascota

saludo = ser.getSaludo()
print("Todo ok, " + saludo)

m1 = ser.getMascota1()
m2 = ser.getMascota2()
print(m1.nombre)
print(m2.nombre)