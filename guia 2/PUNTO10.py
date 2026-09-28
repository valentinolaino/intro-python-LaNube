# Leer una lista de 8 números enteros y mostrar el mayor y el menor.

print('INGRESE 8 NÚMEROS ENTEROS:')
numeros = []
for i in range(8):
    print(f'INGRESE EL NÚMERO {i + 1}:')
    numero = int(input())
    numeros.append(numero)

print(f'El mayor número es: {max(numeros)}')
print(f'El menor número es: {min(numeros)}')