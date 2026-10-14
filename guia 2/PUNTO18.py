# Cada estudiante tiene un nombre y una lista de materias. Mostrar los alumnos que cursan más de 3 materias.
estudiantes = [
    {"nombre": "Juan", "materias": ["Matemáticas", "Física", "Química"]},
    {"nombre": "Axel", "materias": ["Química", "Lengua", "Geografía"]},
    {"nombre": "Pablo", "materias": ["Inglés", "Portugués"]},
    {
        "nombre": "Mauricio",
        "materias": ["Biología", "Prácticas Edúcativas", "Química", "Inglés"],
    },
    {"nombre": "Patricio", "materias": ["Matemáticas"]},
]

for estudiante in estudiantes:
    if len(estudiante["materias"]) > 3:
        print(f"El estudiante {estudiante['nombre']} cursa más de 3 materias.")
