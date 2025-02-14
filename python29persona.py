from class29persona import Persona

print("Ejemplo clases persona")
person = Persona()
person.pais = "España"
print("Pais: " + person.pais)
person.nombre = "José"
person.apellidos = "Risu"
print(person.getDescripcion("Hola caracola"))
person.email = "jr@gmail.com"
person.anyonacimiento = 1989
print(person.getNombreCompleto())
print("Edad: " + str(person.getEdad()))
person2 = Persona()
print("Pais persona 2 " + person2.pais)
print("Fin de programa")
print(person)