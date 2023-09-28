frase = input("introduzca una frase ")
vocal = input("introdruzca una vocal ")

if len(vocal) == 1 and vocal in "aeiouAEIOU":
    frase_modificada = frase.replace(vocal.lower(),vocal.upper())
    print ("Frase con la vocal mayúscula ",frase_modificada)
else:
    print("Por favor introduce una única vocal (a,e,i,o,u).")