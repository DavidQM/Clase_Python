# -*- coding: utf-8 -*-
"""
Fecha: 21/06/2017
Autor: David Q
Titulo:
Descipcion: programa para encontrar el area de figuras geometricas

"""
from math import pi

print("Programa que calcula el area de diversas figuras geometricas")
print("Menu")
print("1.Rectamgulo")
print("2.Circulo")
print("3.Trapecio")
print("4.Triangulo")

opcion = int(input("Señeleccione opcion:"))

if(opcion==1):
    b=float(input("Ingrese la base:"))
    a=float(input("Ingrese la altura:"))
    Area=b * a
elif(opcion==2):
    r=float(input("Ingrese el radio:"))
    Area= pi*(r**2)
elif (opcion == 3):
    b1 = float(input("Ingrese la base mayor:"))
    b2 = float(input("Ingrese la base menor:"))
    a= float(input("Ingrese la altura"))
    Area=((b1+b2)*a)/2
elif (opcion == 4):
    b = float(input("Ingrese la base:"))
    a = float(input("Ingrese la altura:"))
    Area =(b*a)/2


print("El area es:", Area)