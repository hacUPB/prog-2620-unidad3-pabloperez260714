def menu():
opcion = 0
while opcion < 1 or opcion > 4: 
    print("1. Suma/n2. Resta/n3. Multiplicación/n4 División")
    opcion = int(input("seleccione una opcion: "))
    if opcion < 1 or opcion > 4:
        print("la opcion no es valida")
    return opcion 
operacion = menu()
print(f"El usuario eligió la opcion {operacion}")
if operacion == 1:
    
if operacion == 2:
    pass
if operacion == 3:
    pass
if operacion == 4:
