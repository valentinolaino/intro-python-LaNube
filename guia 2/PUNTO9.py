# Ingresar una lista de 10 números y mostrar el promedio.

print('INGRESE 10 NÚMEROS:')
numeros = []
for i in range(10):
      print(f'INGRESE EL NÚMERO {i + 1}:')
      numero = float(input())
      numeros.append(numero)

promedio = sum(numeros) / len(numeros)
print(f'El promedio de los números ingresados es: {promedio}')