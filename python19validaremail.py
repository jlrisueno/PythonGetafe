print("Validar email")
print("Introduce email:")
mail = input()
if(mail.find("@")==-1):
    print("Falta @")
elif(mail.find(".")==-1):
    print("Falta PUNTO")
#elif(mail.startswith("@")==true or mail.endswith("@")==true):
#   print("El email no puede empezar ni terminar por @")
elif(mail[0]=="@"):
    print("El email no puede empezar por @")
elif(mail[0]=="."):
    print("El email no puede empezar por PUNTO")
elif(mail[(len(mail))-1]=="@"):
    print("El email no puede terminar por @")
elif(mail[(len(mail))-1]=="."):
    print("El email no puede terminar por PUNTO")
elif(mail.find(".",mail.find("@"))==-1):
    print("Tiene que haber un punto después del @")
elif(len(mail)-(mail.rfind(".")+1) < 2):
    print("El dominio debe de ser de 2 a 3 caractéres")
elif(len(mail)-(mail.rfind(".")+1) > 3):
    print("El dominio debe de ser de 2 a 3 caractéres")
elif(mail.rfind("@")!=mail.find("@")):
    print("No puede tener más de un @")
print("Fin de programa")