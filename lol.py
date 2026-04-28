import time
import random

posicion=0
meta=50
turnos=1

while posicion<meta:
    
    dado1= random.randint(1,6)
    dado2= random.randint(1,6)
    print(f"el primer dado dio {dado1}")
    print(f"el segundo dado dio {dado2}")
    posicion+=dado1+dado2
    time.sleep(1)
    print(f"el jugador esta en la posicion {posicion}")
    turnos+=1
print("ha llegado a la meta")