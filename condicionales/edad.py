edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 125: 
    if edad < 6:
        etapa = "infancia"
    elif edad < 12:
        etapa = "niñez"
    elif edad < 20:
        etapa = "adolescencia"
    elif edad < 25:
        etapa = "juventud"
    elif edad < 60:
        etapa = "adultez"
    else:
        etpa = "vejez"
    print (f"A sus {edad} años, usted está en la etapa de {etapa}")

else: 
    print("El número ingresado no es una edad válida")


### elif sirve para poner varias condiciones en cadena sin necesidad del if 