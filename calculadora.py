def suma (n1,n2):
    return n1+n2
def resta (n1,n2):
    return n1-n2
def multiplicacion (n1,n2):
    return n1*n2
def division (n1,n2):
    return n1/n2
#comienzo del programa
n1=float(input("Ingrese el primer numero "))
n2=float(input("Ingrese el segundo numero "))
decision=int(input("Ingrese 1 si quiere suma, 2 para resta, 3 para multiplicación y 4 para división "))
if n2!=0:
    if decision==1:
        print suma(n1,n2)
    elif decision==2:
        print resta(n1,n2)
    elif decision==3:
        print multiplicacion(n1,n2)
    elif decision==4:
        print division(n1,n2)
    else:
        print ("error, no ingresaste un número correcto")
else:
    print("no se puede dividir por 0")
