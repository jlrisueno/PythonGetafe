print("Calcular letra DNI")
print("Introduzca DNI:")
varDNI = int(input())
#varResult = varDNI-(int(varDNI/23)*23)
varResult = varDNI%23
if(varResult == 0):
    print("T")  
elif(varResult == 1):
    print("R")
elif(varResult == 2):
    print("W")
elif(varResult == 3):
    print("A")
elif(varResult == 4):
    print("G")
elif(varResult == 5):
    print("M")
elif(varResult == 6):
    print("Y")  
elif(varResult == 7):
    print("F")
elif(varResult == 8):
    print("P")
elif(varResult == 9):
    print("D")
elif(varResult == 10):
    print("X")
elif(varResult == 11):
    print("B")
elif(varResult == 12):
    print("N")
elif(varResult == 13):
    print("J")
elif(varResult == 14):
    print("Z")
elif(varResult == 15):
    print("S")
elif(varResult == 16):
    print("Q")
elif(varResult == 17):
    print("V")
elif(varResult == 18):
    print("H")
elif(varResult == 19):
    print("L")
elif(varResult == 20):
    print("C")
elif(varResult == 21):
    print("K")
elif(varResult == 22):
    print("E")
else:
    print("T")
print("Fin de programa")