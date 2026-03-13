n1 = int(input("ingrese el primer numero entero: "))
n2 = int(input("ingrese el segundo numero entero: "))
if n1 > n2:
    mayor = n1
    menor = n2
else: 
    mayor = n2
    menor = n1

while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
    menor =+ 1