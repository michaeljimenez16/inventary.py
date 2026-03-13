# inventary.py

nombre= input("Ingrese el nombre del productor: ")

while True:
    try:
        precio= float(input(f"Ingrese el precio de {nombre}: "))
        break
    except ValueError: 
        print("Error: Por favor, ingrese un numero decimal valido para el precio.")

while True:
    try:
        cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
        break
    except ValueError:
        print("Error: Por favor, ingrese un numero entero valido para la cantidad.")

costo_total= precio * cantidad

print(f"Producto: {nombre}) | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")
