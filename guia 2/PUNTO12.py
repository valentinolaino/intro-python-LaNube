# Cargar una lista de productos y preguntar al usuario por un nombre. Indicar si está o no en la lista.
productos = []
for i in range(5):
    print(f'INGRESE EL NOMBRE DEL PRODUCTO {i + 1}:')
    producto = input()
    productos.append(producto)

nombre_buscado = input('INGRESE EL NOMBRE DEL PRODUCTO A BUSCAR: ')
if nombre_buscado in productos:
    print(f'El producto "{nombre_buscado}" está en la lista.')
else:
    print(f'El producto "{nombre_buscado}" no está en la lista.') 