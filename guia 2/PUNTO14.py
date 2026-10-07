# Ingresar una lista con números repetidos y mostrar la misma lista sin repeticiones.
numeros = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
numeros_sin_repeticiones = list(set(numeros))
print(f"La lista con repeticiones es: {numeros}")
print(f"La lista sin repeticiones es: {numeros_sin_repeticiones}")
