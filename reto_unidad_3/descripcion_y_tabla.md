#### *Pablo Peréz Mejía ID:000571000*  
#### *Martín Rivera  Salazar ID:000584194*  
 
 
En este reto responderemos a la pregunta: ¿Cómo podemos utilizar la lógica computacional para predecir el consumo de combustible de una aeronave en tiempo real y tomar decisiones de desvío automático que garanticen la seguridad del vuelo?  
Haremos esto por medio de los conocimientos adquiridos en clase, entregando una tabla de análisis, un código y un diagrama de flujo.
 
## tabla de variables 
| variable | tipo | descripcion | 
|----------|------|-------------| 
|  numero_tramos  | entrada  | este es el numero de tramos que se van a realizar en el vuelo  |  
| distancia_tramos  | entrada  | la distancia de cada tramo en kilometros  |
|  viento  | entrada  | que tipo de viento quiere escoger (headwind, tailwind, crosswind)
|  consumo_base  |  constante  |  es el consumo de combustible que va a tener el avion por kilometro  |  
|  ajuste  | constante  | es el porcentaje que afecta el combustible de acuerdo al viento  |
|  capacidad_inicial  |  constante  | capacidad de combustible estandar del A320  |  
|  reserva  |  constante  | es la cantidad de combustible limite  |
|  combustible_actual  | salida  | es el combustible actual del avion  |
| consumo | salida | es el combustible consumido por cada tramo  |
| alerta | salida | es el mensaje que se muestra cuando el combustible cae por debajo de lo establecido  |
| estado_alerta | salida  | es el que indica si el vuelo fue completado o abortado  |