print("Conjetura de Collatz")
print("Introduce un número")
num = int(input())
while(num != 1):
    if(num%2==0):
        num = int(num/2)
    else:
        num = (num*3)+1
    print(num)
print("Fin de programa")