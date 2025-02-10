from math import trunc
print("Día de nacimiento")
print("Introduzca día:")
varDia = int(input())
print("Introduzca mes:")
varMes = int(input())
print("Introduzca año:")
varAno = int(input())
if(varMes == 1):
    varMes = 13
    varAno = varAno-1
elif(varMes == 2):
    varMes = 14
    varAno = varAno-1
varUno = trunc(((varMes+1)*3)/5)
varDos = trunc(varAno/4)
varTres = trunc(varAno/100)
varCuatro = trunc(varAno/400)
varCinco = trunc(varDia+(varMes*2)+varAno+varUno+varDos-varTres+varCuatro+2)
varSeis = trunc(varCinco/7)
varSiete = trunc((varCinco-(varSeis*7)))
if(varSiete == 0):
    print("Sábado")  
elif(varSiete == 1):
    print("Domigo")
elif(varSiete == 2):
    print("Lunes")
elif(varSiete == 3):
    print("Martes")
elif(varSiete == 4):
    print("Miércoles")
elif(varSiete == 5):
    print("Jueves")
else:
    print("Viernes")
print("Fin de programa")