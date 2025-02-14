class Mes:
    nombre = ""
    tempMaxima = 0
    tempMinima = 0

    def __str__(self):
        return "Mes de " + self.nombre + " con máximas de " + str(self.tempMaxima) + " y mínimas de " + str(self.tempMinima)

    def getTemperaturaMedia(self):
        return (self.tempMaxima + self.tempMinima) / 2