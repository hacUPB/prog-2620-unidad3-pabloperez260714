compra = int(input("ingrese el valor de la compra: "))
total = compra + 9000
if compra > 100000:
    total = compra 
print(f"El valor a pagar es ${total}")

envio = 0 
if compra < 1000000:
    envio = 9000
total = compra + envio 

print (f"el valor a pagar es ${total}")
