# Cargar una lista donde cada elemento sea un diccionario con nombre y nota. Mostrar los nombres de los alumnos aprobados.
alumnos = []
diccionario = {"nombre": "Juan", "nota": 8, "aprobado": True}
diccionario2 = {"nombre": "Pedro", "nota": 4, "aprobado": False}
alumnos.append(diccionario)
alumnos.append(diccionario2)
print("Los alumnos aprobados son:")
for alumno in alumnos:
    if alumno["aprobado"]:
        print(alumno["nombre"])
