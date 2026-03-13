INICIO

capacidad_inicial = 158790

    Definir consumo_base = 6

    Definir ajuste = 0.16

    Definir reserva = 20000

    FUNCION calcular_consumo_tramo(distancia, viento)

        consumo = distancia * consumo_base

        SI viento = "headwind" ENTONCES

            consumo = consumo * (1 + ajuste)

        SINO SI viento = "tailwind" ENTONCES

            consumo = consumo * (1 - ajuste)

        SINO SI viento = "crosswind" ENTONCES

            consumo = consumo

        FIN SI

        RETORNAR consumo

    FIN FUNCION

    Leer numero_tramos

    combustible_actual = capacidad_inicial

    Mostrar "SIMULACIÓN DE VUELO SMCS"

    PARA tramo DESDE 1 HASTA numero_tramos HACER

        Mostrar "Tramo", tramo

        Leer distancia

        Leer viento

        consumo = calcular_consumo_tramo(distancia, viento)

        combustible_actual = combustible_actual - consumo

        Mostrar "Consumo del tramo:", consumo

        Mostrar "Combustible restante:", combustible_actual

        SI combustible_actual <= reserva ENTONCES

            Mostrar "ALERTA CRÍTICA"

            Mostrar "El combustible está por debajo de la reserva legal"

            Mostrar "Abortar misión y aterrizar en aeropuerto alterno"

            SALIR DEL CICLO

        FIN SI

    FIN PARA

    SI combustible_actual > reserva ENTONCES

        Mostrar "Vuelo completado con éxito"

        Mostrar "Combustible final:", combustible_actual

    FIN SI

FIN
 
INICIO

capacidad_inicial = 158790

consumo_base = 6

ajuste = 0.16

reserva = 20000

    FUNCION calcular_consumo_tramo(distancia, viento)

        consumo = distancia * consumo_base

        SI viento = "headwind" ENTONCES

            consumo = consumo * (1 + ajuste)

        SINO SI viento = "tailwind" ENTONCES

            consumo = consumo * (1 - ajuste)

        SINO SI viento = "crosswind" ENTONCES

            consumo = consumo

        FIN SI

        RETORNAR consumo

    FIN FUNCION

    Leer numero_tramos

    combustible_actual = capacidad_inicial

    Mostrar "SIMULACIÓN DE VUELO SMCS"

    PARA tramo DESDE 1 HASTA numero_tramos HACER

        Mostrar "Tramo", tramo

        Leer distancia

        Leer viento

        consumo = calcular_consumo_tramo(distancia, viento)

        combustible_actual = combustible_actual - consumo

        Mostrar "Consumo del tramo:", consumo

        Mostrar "Combustible restante:", combustible_actual

        SI combustible_actual <= reserva ENTONCES

            Mostrar "ALERTA CRÍTICA"

            Mostrar "El combustible está por debajo de la reserva legal"

            Mostrar "Abortar misión y aterrizar en aeropuerto alterno"

            SALIR DEL CICLO

        FIN SI

    FIN PARA

    SI combustible_actual > reserva ENTONCES

        Mostrar "Vuelo completado con éxito"

        Mostrar "Combustible final:", combustible_actual

    FIN SI

FIN
 