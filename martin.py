# suma=0
# notas=int(input("ingrese la cantidad de notas "))
# for i in range(notas):
#     nota=float(input("ingrese su nota "))
#     suma=suma+nota
#     prom=suma/notas
#     print(f"El promedio es {prom} ")

#     if prom>=4:
#         print("el alumno ha aprovado")
#     else :
#         print("el alumno reprobo")

# num=int(input("ingrese numero:"))
# total=0
# for i in range(num):
#     total=total+i+1
#     print(f"la sumatoria es: {total}")

# num=int(input("ingrese numero:"))
# total=1
# for i in range(num):
#     total=total*(i+1)
#     print(f"la sumatoria es: {total}")



# for i in "lol":
#     print(i)


#contador de vovales y consonantes
# vocales=0
# conso=0
# nombre=(input("ingrese su nombre: "))
# for i in nombre:
#     print (i)
#     if i in "aeiouAEIOU":
#         vocales+=1
#     elif i ==" ":
#         ''''''
#     else:
#         conso+=1
# print(f"el total de vocales es {vocales}")
# print(f"el total de consonantes es {conso}")




can1=input("ingrese canidato 1: ")
can2=input("ingrese canidato 2: ")
voto1=0
voto2=0
num=int(input("ingrese la cantidad de votantes: "))

for i in range (num):
    voto=int(input(f"Por quien votara. 1.-{can1} 2.- {can2} "))
    if voto==1:
        voto1+=1
    elif voto==2:
        voto2+=2
    else:
        print("voto no valido")
if voto1>voto2:
    print(f"el ganador es {can1} con {voto1} votos")
else 