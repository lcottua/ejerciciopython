''' nro = input(" ingresa un nro ")
nro1= int(nro)
while(nro1>0) :
    print(nro1)
    nro1 = nro1 - 1
print("sali")
texto = input(" ingresa un texto ")
while(not texto == "exit") :
    texto = input(" ingresa un texto ")
print("saliste")
'''
contador=0
alumnos = ["anderson", "lizmar","daniel","migdalia","Andres"] # esto es la declaracion de una lista
for alumno in alumnos :
    print(len(alumno))
print("ahora")
for letra in alumnos[0] :
    if letra == "n":
        contador=contador+1
print(contador)
