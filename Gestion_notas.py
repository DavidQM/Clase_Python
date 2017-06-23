#For - promedio
print("Gestor de notas del curso de Python")
N= int(input("Ingrese la cantidad de estudiantes"))
acumCurso=0
acumNotasEstudiante=0
promEstudiante=0
acumLab=0

nota1=-1
nota2=-1
notaLab=-1
gana=0
pierde=0

for i in range(1,N+1,1):
    print("Ingrese estudiante numero",i)
    nota1 = -1
    while(nota1<0 or nota1>=5):
        nota1 = float(input("Ingrese la nota 1 (30%)"))
    nota2 = -1
    while (nota2 < 0 or nota2 >= 5):
        nota2 = float(input("Ingrese la nota 2 (30%)"))
    #nota lab - ciclo anidado
    input("Ingrese las 5 notas del Lab (40%)")
    acumLab=0
    for j in range(1,5+1,1):
        notaLab=-1
        while (notaLab < 0 or notaLab >= 5):
            notaLab=float(input("ingrese nota del lab #"+str(j)+":"))
        acumLab+=notaLab
    nota3 = acumLab/j

    promEstudiante+=(nota1*0.3) +(nota2*0.3) +(nota3*0.4)
    print("el promedio del estudiante",i,"es de",promEstudiante)

    if(promEstudiante>=3):
        gana+=1
    else:
        pierde+=1

    acumCurso += promEstudiante

promCurso=acumCurso/ N
print("El promedio es:",promCurso)

pGana= gana/(N*100)
print("El porcentaje de estudiantes que ganaron fue:",pGana)

pPierde= pierde/(N*100)
print("El ´porcentaje de estudiantes que perdieron fue:",pPierde)
