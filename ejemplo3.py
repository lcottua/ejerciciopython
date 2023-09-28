# ejemplo de uso de if

edad = input(" ingresa tu edad ")

if int(edad) > 2 and int(edad) < 10 :
    print (" eres un nene")

if int(edad) > 18 :
    print (" eres mayor de edad")
    if int(edad) > 40: 
        print (" ademas eres un adulto")
        
elif int(edad) == 18:
    print (" estas en el limite")
else:
    print ( " eres menor" )



