# Solicitar tres notas y mostrar el promedio e indicar si el alumno está aprobado o desaprobado.

print('INGRESE:')
n1 = int(input("La primer nota: "))
n2 = int(input("La segunda nota: "))
n3 = int(input("La tercer nota: "))

promedio = (n1 + n2 + n3) / 3

print(f"El promedio es: {promedio}")

if promedio >= 6:
    print("El alumno está aprobado.")
else:
    print("El alumno está desaprobado.")

