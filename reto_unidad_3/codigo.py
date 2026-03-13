
capacidad_inicial = 158790 
consumo_base = 6             
ajuste = 0.16         
reserva = 20000       
def calcular_consumo_tramo(distancia, viento):   ## aqui usamos ia para saber como poner la definicion y comprendimos que distancia y viento se usan en relacion al calculo que usa la funcion 
    
    consumo = distancia * consumo_base

    if viento == "headwind":
        consumo = consumo * (1 + ajuste)

    elif viento == "tailwind":
        consumo = consumo * (1 - ajuste)

    elif viento == "crosswind":
        consumo = consumo

    return consumo
numero_tramos = int(input("Ingrese el número de tramos del vuelo: "))

combustible_actual = capacidad_inicial

print("\nSIMULACIÓN DE VUELO SMCS")

for tramo in range(1, numero_tramos + 1):

    print("\nTramo", tramo)

    distancia = int(input("Ingrese la distancia del tramo (km): "))
    viento = input("Tipo de viento (headwind / tailwind / crosswind): ")

    consumo = calcular_consumo_tramo(distancia, viento)

    combustible_actual = combustible_actual - consumo

    print("Consumo del tramo:", round(consumo,2), "kg")
    print("Combustible restante:", round(combustible_actual,2), "kg")
    if combustible_actual <= reserva:
        print("\n⚠ ALERTA CRÍTICA")
        print("El combustible está por debajo de la reserva legal")
        print("Abortar misión y aterrizar en aeropuerto alterno")
        break
if combustible_actual > reserva:
    print("\nVuelo completado con éxito")
    print("Combustible final:", round(combustible_actual,2), "kg")