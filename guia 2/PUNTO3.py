# Leer una temperatura en grados Celsius y convertirla a Fahrenheit.
# Ejemplo:
# °F=(°C×1.8)+32
# °F=(25×1.8)+32=45+32=77°F
# Por lo tanto, 25 °C equivalen a 77 °F.

print('INGRESE LA TEMPERATURA EN GRADOS CELSIUS:')
celsius = float(input())
fahrenheit = (celsius * 1.8) + 32
print(f'La temperatura en grados Fahrenheit es: {fahrenheit} °F')
