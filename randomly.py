#Randomly
import random
import time
# time.sleep(1)
# num=random.randint(1,10)
# print(num)

# for i in range (num):
#     print("hola")

# j1 = random.randint(60,190)
# j2 = random.randint(60,190)
# j3 = random.randint(60,190)
# print(f"j1 ha golpeado la pelota, pelota ha avanzado {j1} metros")
# print(f"j2 ha golpeado la pelota, pelota ha avanzado {j2} metros")
# print(f"j3 ha golpeado la pelota, pelota ha avanzado {j3} metros")

# if j1>j2 and j1>j3:
#     print(f"el jugador j1 ha lanzado mas lejos")
# elif j2>j3:
#     print(f"el jugador j2 ha lanzado mas lejos")
# elif j3>j2:
#     print(f"el jugador j3 ha lanzado mas lejos")
# else:
#     print("los jugadores han empatado")


# dado1= random.randint(1,6)
# dado2= random.randint(1,6)
# print(f"el primer dado dio {dado1}")
# print(f"el segundo dado dio {dado2}")

# if dado1 == dado2:
#     print ("vayase a la carcel")
# else:
#     print("suerte.")






# posicion=0
# meta=50
# turnos=1

# while posicion<meta:
    
#     dado1= random.randint(1,6)
#     dado2= random.randint(1,6)
#     print(f"el primer dado dio {dado1}")
#     print(f"el segundo dado dio {dado2}")
#     posicion+=dado1+dado2
#     time.sleep(1)
#     print(f"el jugador esta en la posicion {posicion}")
#     turnos+=1
# print("ha llegado a la meta")



# num=random.randint (1,100)
# numUsu=int(input("adivine el numero"))

# if num==numUsu:
#     print("has adivinado el numero!!")
# elif numUsu>num:
#     print("te has pasado")
# else:
#     print ("te ha faltado")

# print("loteria, adivina los 3 numeros ganadores")
# print("inserta numeros del 1 al 9")
# num1=random.randint (1,9)
# num2=random.randint (1,9)
# num3=random.randint (1,9)
# print(f"{num1}{num2}{num3}")
# numUsu1=int(input(" adivine el numero 1 "))
# numUsu2=int(input(" adivine el numero 2 "))
# numUsu3=int(input(" adivine el numero 3 "))
# if num1==numUsu1 and num2==numUsu2 and num3==numUsu3 :
#     print("has adivinado el numero!!")


# num1=random.randint (1,9)
# num2=random.randint (1,9)
# num3=random.randint (1,9)
# t1=False
# t2=False
# t3=False
# print(f"los numeros generados son {num1}")



# print("venta de latas nacionales")
# lata=int(input("insertar el peso de la lata (gr)"))
# while lata>=0:
#     print("error, insertar valor positivo")
#     lata=int(input("insertar el peso de la lata (gr)"))
# sodio=int(input("ingrese la cantidad de sodio (gr)"))
# while sodio not in range(1,100):
#     print("error, el sodio tiene que ser entre 1gr a 100gr")
#     sodio=int(input("ingrese la cantidad de sodio (gr)"))
# if lata>500:
#     print("es una lata normal")
# elif lata>501 and lata<1500:
#     print(" es una lata mediana")
# elif lata<1501:
#     print("es una lata grande")


peces=random.randint(10,20)
pLata=0
pPlancha=0
for p in range(peces):
    pesoP=random.randint(100,2000)
    if pesoP<800:
        pLata+=1
    else:
        pPlancha+=1
        



