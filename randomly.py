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



num=random.randint (1,100)
numUsu=int(input("adivine el numero"))

if num==numUsu:
    print("has adivinado el numero!!")
elif numUsu>num:
    print("te has pasado")
else:
    print ("te ha faltado")

