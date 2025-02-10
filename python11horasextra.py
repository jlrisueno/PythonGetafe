print("Ejemplo horas extra:")
print("Introduzca las horas trabajadas:")
horas = int(input())
print("Introduzca los km realizados:")
km = int(input())
print("Introduzca precio/hora:")
precio = int(input())
horasextra = 0
salariobase = 0
salarioextra = 0
salariototal = 0
dietas = ""
retenciones = ""
if(horas > 36):
    horasextra = horas - 36
    salariobase = 36 * precio
    salarioextra = horasextra * (precio+2)
else:
    salariobase = horas * precio
salariototal = salariobase + salarioextra
if(km <= 100):
    dietas = "LOCALES"
elif(km >= 101 and km <= 500):
    dietas = "PROVINCIALES"
else:
    dietas = "NACIONALES"
if(salariototal < 250):
    retenciones = "SIN RETENCIONES"
elif(salariototal >= 250 and salariototal <= 600):
    retenciones = "20% DE RETENCIÓN"
else:
    retenciones = "40% DE RETENCIÓN"
print("Horas:", horas)
print("Horas extras:", horasextra)
print("Salario base:", salariobase)
print("Salario extra:", salarioextra)
print("Salario total:", salariototal)
print("Dietas:", dietas)
print("Retenciones:", retenciones)