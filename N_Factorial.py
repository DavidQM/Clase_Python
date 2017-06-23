# -*- coding: utf-8 -*-
"""
Fecha: 23/06/2017
Autor: David Q
Titulo: N factorial
Descipcion: Aplicacion de Ciclos simples y anidados

"""

print("Factorial")

n=int(input("Ingrese el numero que desea conocer su factoral"))

sumatoria=0
fact=1

for i in range (1,n+1,1):
    sumatoria = sumatoria+i
    fact=fact*i
    print(i,fact)

print("La sumatoria hasta",n,"es:",sumatoria)
print("el factorial de",n,"es:",fact)