# -*- coding: utf-8 -*-
"""
Fecha: 23/06/2017
Autor: David Q
Titulo: Raiz cubica
Descipcion: Aplicacion de Ciclos simples - sln de problemas

"""

print("Raiz Cubica")

n=int(input("Ingrese el numero del que desaea conocer la raiz cubica"))

cubo=0
i=0

while(cubo < abs(n)):
    i+=1
    cubo=i**3

if(cubo==abs(n)):
    if(n<0):
        i*=-1
    print("la raiz cubica de n es:",i)
else:
    print("El numero",n,"no tiene raiz exacta")