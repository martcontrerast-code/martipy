
# def saludo():
#     print("Hola loco")
# #saludo()

# name="monica"

# def chao():
#     print ("hola", name )
# #chao()

# def suma():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(F"el resultado es {n1+n2}")

# suma

# for i in "lol":
#     print(i)
op=0
while op!=4:
    print("elige una opcion")
    print("1.- contador de vocales y consonantes")
    print("2.- TiendaGamer ")
    print("3.- calculadora ")

def contador_de_vocales_y_consonantes():
    vocales=0
    conso=0
    nombre=(input("ingrese su nombre: "))
    for i in nombre:
        print (i)
        if i in "aeiouAEIOU":
            vocales+=1
        elif i ==" ":
            ''''''
        else:
            conso+=1
    print(f"el total de vocales es {vocales}")
    print(f"el total de consonantes es {conso}")

def tiendaGamer():
    op=0
    total=0
    while op!=4:
        print("seleccione una opccion")
        print("1.- xbox $250.000")
        print("2.- sony ps5 $500.000")
        print("3.- LGTV 60 $600.000")
        print("4.- salir")
        op=int(input("selecione una opcion: "))
        match op:
            case 1:
                print("el valor a pagar es,", 250000*1.19)
                total+=250000*1.19
            case 2:
                print("el valor a pagar es", 500000*1.19)
                total+=500000*1.19
            case 3:
                print("el valor a pagar es", 600000*1.19)
                total+=600000*1.19
            case 4:
                print(f"saliendo, su total es {total}")
                
            case _:
                print ("opcion invalida")

def calculadora():

    suma=0
    rest=0
    divi=0
    mult=0
    op=0
    while op!=5:
        print("1.- sumatoria")
        print("2.- divisoria")
        print("3.- multiplicacion")
        print("4.- division ")
        print("5.- salir")
        op=int(input("elija una operacion:"))
        match op:
            case 1:
                n1=int(input("numero 1: "))
                n2=int(input("numero 2: "))
                suma=n1+n2
                print(f"{n1}+{n2}={suma}")
            case 2:
                n1=int(input("numero 1: "))
                n2=int(input("numero 2: "))
                rest=n1-n2
                print(f"{n1}-{n2}={rest}")
            case 3:
                n1=int(input("numero 1: "))
                n2=int(input("numero 2: "))
                mult=n1*n2
                print(f"{n1}*{n2}={mult}")
            case 4:
                n1=int(input("numero 1: "))
                n2=int(input("numero 2: "))
                divi=n1/n2
                print(f"{n1}/{n2}={divi}")
            case 5:
                print("saliendo de la calculadora")
            case _:
                print("opcion invalida")


            


