def factorial(numero):
    if numero < 0:
        print ("error")
    else: 
        acumulador = 1
        for factor in range (1,numero+1):
            acumulador = acumulador * factor

        return acumulador
resultado = factorial (6)
print(resultado)