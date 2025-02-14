from class30conductor import Coche

class Derpotivo(Coche):
    
    def turbo(self):
        self.velocidad += 120
        print("Velocidad", + self.velocidad)
        print("Turbo activado!!")

    def acelerar(self):
        if(self.estado == False):
            print("El coche no está arrancado. Debe arrancar antes")
        else:
            self.velocidad += 60
        print("Velocidad actual " + str(self.velocidad))

    def getVelocidadMaxima(selt):
        velocidadCoche = super().getVelocidadMaxima()
        return velocidadCoche + 100