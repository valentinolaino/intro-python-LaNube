# Cargar una lista con 5 números y mostrar la suma total.

print('INGRESE 5 NÚMEROS:')
numeros = []
for i in range(5):
    print(f'INGRESE EL NÚMERO {i + 1}:')
    numero = float(input())
    numeros.append(numero)

print(f'La suma total es: {sum(numeros)}')
