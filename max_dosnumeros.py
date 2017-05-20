#metodo max dos numeros

num1= int(input("ingrese un numero"))
num2= int(input("ingrese otro numero"))
mMax = max(num1,num2)
print (mMax)
def max (num1, num2):
    if num1 < num2:
        print (num2)
    elif num2 < num1:
        print (num1)
    else:
        print ("Son iguales")
