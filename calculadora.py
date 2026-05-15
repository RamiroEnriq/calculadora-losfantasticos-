def suma (n1,n2):
    return n1+n2
def resta (n1,n2):
    return n1-n2
def multiplicacion (n1,n2):
    return n1*n2
#comienzo del programa
while True: #para retroalimentacion del codigo
    print("---seleccione una opcion---")
    opcion=int(input(" sumar [ 1] restar [ 2 ] multiplicar [ 3 ] dividir [ 4 ] o salir [ 5 ] : "))
    if opcion == 5:#termina solo si el usuario decide terminar, sino NO
        print("---saliendo de la  calculadora...---")
        break
    if opcion==1 or opcion==2 or opcion==3 or opcion==4:
        n1 = float(input("ingrese el primer numero: "))
        n2 = float(input("ingrese el segundo numero: "))

        #este bloque se conecta con las respectivas funciones
        if opcion == 1:
            print("resultado:  ", suma(n1, n2))
        elif opcion == 2:
            print("resultado:  ", resta(n1, n2))
        elif opcion == 3:
            print("resultado:  ", multiplicacion(n1, n2))
        elif opcion == 4:
            print("resultado:  ", division(n1, n2))
        else:
            print ("---opcion NO valida---")

