articulo_1 = int(input("Ingrese el precio del articulo 1: " ))
articulo_2 = int(input("ingrese el precio del articulo 2: "))
articulo_3 = int(input("ingrese el precio del articulo 3: "))
if articulo_1 < articulo_2 and articulo_2 < articulo_3:
    descuento = articulo_1 * 0.50
    menor = articulo_1 - descuento
    print (f"el articulo menor es:{total}")
    suma = menor + articulo_2 + articulo_3
else:
    if articulo_2 < articulo_1 and articulo_1 < articulo_3:
        descuento = articulo_2 * 0.50
        menor = articulo_2 - descuento
        total = menor + articulo_1 + articulo_3
        print(f"el articulo menor es el articulo 2{total}")
    else:
        descuento = articulo_3 * 0.5
        menor = articulo_3 - descuento
        total = menor + articulo_1 + articulo_2
        print(f"el articulo menor es el articulo 3: {total}")
