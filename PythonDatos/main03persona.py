from services import service03personas as person
from models import persona

p1 = person.getPersona()
print(f"{p1.nombre} de {p1.edad} años con email: {p1.email}")