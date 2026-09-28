# Solicitar al usuario ingresar 5 nombres y luego imprimirlos en orden inverso.

nombres = []
for i in range(5):
      print(f'INGRESE EL NOMBRE {i + 1}:')
      nombre = input()
      nombres.append(nombre)

print('Nombres en orden inverso:')
for nombre in reversed(nombres):
      print(nombre)

