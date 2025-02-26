from models import mascota

def getSaludo():
    return "Bienvenido a Matrix"

def getMascota1():
    dato = mascota.Mascota()
    dato.nombre = "Ari"
    dato.raza = "Perrita"
    dato.edad = 9
    return dato

def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Sulio"
    dato.raza = "Perro"
    dato.edad = 3
    return dato