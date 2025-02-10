print("Ejemplo mayor tres números:")
print("Introduzca número 1:")
num1 = int(input())
print("Introduzca número 2:")
num2 = int(input())
print("Introduzca número 3:")
num3 = int(input())
mayor = 0
menor = 0
intermedio = 0
if(num1 >= num2 and num1 >= num3):
    mayor = num1
elif(num2 >= num1 and num2 >= num3):
    mayor = num2
else:
    mayor = num3
if(num1 <= num2 and num1 <= num3):
    menor = num1
elif(num2 <= num1 and num2 <= num3):
    menor = num2
else:
    menor = num3
suma = num1 + num2 + num3
intermedio = suma - mayor - menor
print("Mayor:", mayor)
print("Intermedio:", intermedio)
print("menor:", menor)