from models import persona

def getPersona():
    dato = persona.Persona()
    dato.nombre = "José"
    dato.edad = 35
    dato.email = "jr@gmail.com"
    return dato