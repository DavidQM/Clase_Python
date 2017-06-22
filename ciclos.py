# -*- coding: utf-8 -*-
"""
Fecha: 22/06/2017
Autor: David Q
Titulo: Ciclos
Descipcion: Aplicacion de Ciclos simples y anidados

"""

""""
print("programa que muestra los primeros numeros N")
N= int(input("Ingrese el valor de N"))
cont =1
while(cont <= N):
    print("contador:",cont)
    cont+=1
print("fin del programa")

"""
"""
# cuantitativa
print("programa que muestra los primeros numeros N (sin mostrar los multiplos de 3, pero suma los multiplos de 3)")
N= int(input("Ingrese el valor de N"))
sum=0
cont =1
while(cont <= N):
    if(cont % 3 != 0):
        print("contador:",cont)
    else:
        sum+=cont
    cont+=1
print("La suma de los multiplos de 3 hasta el numero",N,"es",sum)
print("fin del programa")
"""
"""
#cualitativa

print("suma de datos")

suma=0
opc="si"
i=1
while(opc=="si"):
    dato=float(input("Ingrese dato "+str(i)+" a sumar :"))
    suma+=dato
    i+=1
    opc=str(input("Desea ingresar un nuevo dato? (si o no)"))
print("La suma es",suma)
print("Find el programa")
"""
"""
#dato sentinela - cualitativa
print("suma de datos")

suma=0
dato=0
i=1
while(dato != -1):
    dato=float(input("Ingrese dato "+str(i)+" a sumar : (-1 para salir)"))
    suma+=dato
    i+=1

print("La suma es",suma)
print("Find el programa")
"""
"""
#ciclo For - mas amigable para las condiciones cuantitativas
print("programa que muestra los primeros numeros N")
N= int(input("Ingrese el valor de N"))

for i in range(1,N+1,1):# siempre llega menor a N - no es nunca <_=
    print(i)

print("fin del programa")
"""

#For - promedio
print("Gestor de notas del curso de Python")
N= int(input("Ingrese la cantidad de estudiantes"))
acumCurso=0
acumNotasEstudiante=0
promEstudiante=0
acumLab=0

for i in range(1,N+1,1):
    print("Ingrese estudiante numero",i)
    nota1 = float(input("Ingrese la nota 1 (30%)"))
    nota2 = float(input("Ingrese la nota 2 (30%)"))
    #nota lab - ciclo anidado
    input("Ingrese las 10 notas del Lab (40%)")
    acumLab=0
    for j in range(1,10+1,1):
        notaLab=float(input("ingrese nota del lab #"+str(j)+":"))
        acumLab+=notaLab
    nota3 = acumLab/j

    promEstudiante+=(nota1*0.3) +(nota2*0.3) +(nota3*0.4)
    print("el promedio del estudiante",i,"es de",promEstudiante)
    acumCurso += promEstudiante

promCurso=acumCurso/ N

print("El promedio es:",promCurso)
