# Crear una lista de productos, cada uno con nombre, precio y stock. Mostrar el total de productos con stock menor a 5.
productos = [
    {"nombre": "Producto 1", "precio": 10.0, "stock": 3},
    {"nombre": "Producto 2", "precio": 15.0, "stock": 7},
    {"nombre": "Producto 3", "precio": 20.0, "stock": 2},
    {"nombre": "Producto 4", "precio": 25.0, "stock": 10},
]

for producto in productos:
    if producto["stock"] < 5:
        print(
            f"El producto {producto['nombre']} tiene un stock menor a 5, el cual es: {producto['stock']}"
        )
