
file= open("texto1.txt","r")
print("Nombre:",file.name)
#leer el archivo e imprimir

print("1. leyendo archivo :")
contenido = file.read()
print(contenido)

print("2. leyendo archivo :")
contenido = file.read()
print(contenido)

file.seek(1)
print("3. leyendo archivo :")
contenido = file.read()
print(contenido)

file.seek(0)
print("4. leyendo archivo :")
contenido = file.read()
print(contenido)
