class Persona:
    nombre = ""
    apellidos = ""
    email = ""
    anyonacimiento = 0
    pais = ""

    def __init__(self):
        self.pais = "Elantris"

    def __str__(self):
        return self.apellidos + " " + self.nombre + ", " + self.pais

    def getDescripcion(self, descripcion):
        return self.getNombreCompleto() + ", " + descripcion

    def getNombreCompleto(self):
        return self.nombre + " " + self.apellidos

    def getEdad(self):
        return 2025 - self.anyonacimiento