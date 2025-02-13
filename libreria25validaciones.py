def validarISBN(isbn):
    longitud = len(isbn)
    if(longitud !=10):
        print("Debe introducir un ISBN de 10 dígitos")
        return "INCORRECTO"
    elif(isbn.isdigit() == False):
        print("El número ISBN debe contener solo números")
        return "INCORRECTO"
    else:
        multi = 0
        for i in range(longitud):
            multi = multi + (int(isbn[i])*(i+1))
        if(multi%11==0):
            return "CORRECTO"
        else:
            return "INCORRECTO"

def letraDNI(varDNI):
    varResult = varDNI-(int(varDNI/23)*23)
    if(varResult == 0):
        return "T" 
    elif(varResult == 1):
        return "R" 
    elif(varResult == 2):
        return "W" 
    elif(varResult == 3):
        return "A" 
    elif(varResult == 4):
        return "G" 
    elif(varResult == 5):
        return "M" 
    elif(varResult == 6):
        return "Y" 
    elif(varResult == 7):
        return "F" 
    elif(varResult == 8):
        return "P" 
    elif(varResult == 9):
        return "D" 
    elif(varResult == 10):
        return "X" 
    elif(varResult == 11):
        return "B" 
    elif(varResult == 12):
        return "N" 
    elif(varResult == 13):
        return "J" 
    elif(varResult == 14):
        return "Z" 
    elif(varResult == 15):
        return "S" 
    elif(varResult == 16):
        return "Q" 
    elif(varResult == 17):
        return "V" 
    elif(varResult == 18):
        return "H" 
    elif(varResult == 19):
        return "L" 
    elif(varResult == 20):
        return "C" 
    elif(varResult == 21):
        return "K" 
    elif(varResult == 22):
        return "E" 
    else:
        return "T" 