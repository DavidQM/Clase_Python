# -*- coding: utf-8 -*-
"""
Fecha: 23/06/2017
Autor: David Q
Titulo: Raiz cuadrada
Descipcion: Aplicacion de Ciclos simples - sln de problemas

"""

print("Raiz Cudrada")

n=float(input("Ingrese el numero del que desaea calcular la raiz cuadrada"))
e=float(input("Ingrese el margen de error"))

#e=0.01
delta=e**2
raiz=0
i=0
cuad=0
dif=abs(n-cuad)

while(dif>e):
    raiz += delta
    cuad=raiz**2
    dif = abs(n - cuad)
    i+=1

print("la raiz cuadrada de",n,"es:",raiz)
print("numero de iteraciones",i)