def sumarNumeros(num1, num2):
    return num1 + num2

def getNumeroComprobado():
    print("Introduzca numero")
    # ALMACENAR LO QUE HA ESCRITO EL USUARIO
    # EN UNA VARIABLE STRING
    aux = input()
    while (aux.isdigit() == False):
        print("Esto no es un numero")
        print("Introduzca numero")
        aux = input()           
    num = int(aux)
    return num