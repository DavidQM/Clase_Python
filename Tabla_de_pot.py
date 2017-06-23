# -*- coding: utf-8 -*-
"""
Fecha: 23/06/2017
Autor: David Q
Titulo: Tabla de potencias
Descipcion: Aplicacion de Ciclos simples - sln de problemas

"""

print("Tabla De Potencias")

LI=int(input("Ingrese el limite inferior"))
LS=int(input("Ingrese el limite superior"))

print("N\tCuad\tCubo")
for i in range (LI,LS+1,1):
    num=i
    cuad=i**2
    cubo=i**3
    print(num,"\t",cuad,"\t",cubo)

print("fin del programa")