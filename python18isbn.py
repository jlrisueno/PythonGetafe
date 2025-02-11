print("Práctica ISBN")
print("Introduce número ISBN:")
isbn = input()
longitud = len(isbn)
if(longitud !=10):
    print("Debe introducir un ISBN de 10 dígitos")
elif(isbn.isdigit() == False):
    print("El número ISBN debe contener solo números")
else:
    multi = 0
    for i in range(longitud):
        multi = multi + (int(isbn[i])*(i+1))
    if(multi%11==0):
        print("CORRECTO")
    else:
        print("INCORRECTO")
print("Fin de práctica")