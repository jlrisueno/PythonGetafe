print("Validar email")
print("Introduce email:")
mail = input()
if(mail.find("@")==-1):
    print("Falta @")
if(mail.find(".")==-1):
    print("Falta PUNTO")
if(mail[0]=="@"):
    print("El email no puede empezar por @")
if(mail[0]=="."):
    print("El email no puede empezar por PUNTO")
if(mail[(len(mail))-1]=="@"):
    print("El email no puede terminar por @")
if(mail[(len(mail))-1]=="."):
    print("El email no puede terminar por PUNTO")
if(mail.find(".",mail.find("@"))==-1):
    print("Tiene que haber un punto después del @")
if(len(mail)-(mail.rfind(".")+1) < 2):
    print("El dominio debe de ser de 2 a 3 caractéres")
if(len(mail)-(mail.rfind(".")+1) > 3):
    print("El dominio debe de ser de 2 a 3 caractéres")
if(mail.rfind("@")!=mail.find("@")):
    print("No puede tener más de un @")
print("Fin de programa")