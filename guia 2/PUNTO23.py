# Crear una lista de alumnos (nombre, DNI) y una lista de cursos (nombre del curso, cupo). El usuario podrá inscribir alumnos en cursos si hay cupos
# disponibles. Al finalizar, mostrar:
# ● Listado de alumnos por curso.
# ● Cursos que aún tienen cupos.
# ● Cantidad total de inscriptos.

alumnos = []
cursos = []


def agregar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    dni = input("Ingrese el DNI del alumno: ")
    alumno = {"nombre": nombre, "dni": dni}
    alumnos.append(alumno)


def agregar_curso():
    nombre = input("Ingrese el nombre del curso: ")
    cupo = int(input("Ingrese el cupo del curso: "))
    curso = {"nombre": nombre, "cupo": cupo, "inscriptos": []}
    cursos.append(curso)


def inscribir_alumno():
    dni = input("Ingrese el DNI del alumno a inscribir: ")
    nombre_curso = input("Ingrese el nombre del curso: ")

    if cursos["nombre"].lower() == nombre_curso.lower():
        if cursos["cupo"] > 0:
            for alumno in alumnos:
                if alumno["dni"] == dni:
                    cursos["inscriptos"].append(alumno)
                    cursos["cupo"] -= 1
                    print(
                        f"El alumno {alumno['nombre']} ha sido inscripto en el curso {cursos['nombre']}."
                    )
                    return
            print("No se encontró un alumno con ese DNI.")
        else:
            print(f"El curso {cursos['nombre']} no tiene cupos disponibles.")


def mostrar_alumnos():
    for curso in cursos:
        print(f"Curso: {curso['nombre']}")
        print("Alumnos inscriptos: ")
        for alumno in curso["inscriptos"]:
            print(f"- {alumno['nombre']} (DNI: {alumno['dni']})")


def cursos_disponibles():
    print("Cursos con cupos disponibles:")
    for curso in cursos:
        if curso["cupo"] > 0:
            print(f"- {curso['nombre']} (Cupos disponibles: {curso['cupo']})")


def total_inscriptos():
    total = 0
    for curso in cursos:
        total += len(curso["inscriptos"])
        print(f"Total de inscriptos en el curso: {total}")
