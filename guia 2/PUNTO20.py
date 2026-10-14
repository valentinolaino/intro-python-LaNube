# Crear un programa que permita registrar libros (título, autor, año y estado: disponible o prestado). El usuario debe poder:
# Agregar nuevos libros.
# Buscar libros por título o autor.
# Prestar un libro (cambiar su estado).
# Mostrar todos los libros disponibles.

libros = [
    {
        "titulo": "El Principito",
        "autor": "Antoine de Saint-Exupéry",
        "año": 1943,
        "estado": "disponible",
    },
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": 1605,
        "estado": "prestado",
    },
    {
        "titulo": "Orgullo y prejuicio",
        "autor": "Jane Austen",
        "año": 1813,
        "estado": "disponible",
    },
    {
        "titulo": "Frankenstein",
        "autor": "Mary Shelley",
        "año": 1818,
        "estado": "prestado",
    },
]


def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año de publicación del libro: "))
    estado = input("Ingrese el estado del libro (disponible/prestado): ")
    libro = {"titulo": titulo, "autor": autor, "año": año, "estado": estado}
    libros.append(libro)


def buscar_libro():
    buscado = input("Ingrese el título o autor del libro que desea buscar: ")
    encontrados = []
    for libro in libros:
        if (
            buscado.lower() in libro["titulo"].lower()
            or buscado.lower() in libro["autor"].lower()
        ):
            encontrados.append(libro)
    return encontrados


def prestar_libro():
    titulo = input("Ingrese el título del libro que desea prestar: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["estado"] == "disponible":
                libro["estado"] = "prestado"
                print(f'El libro "{libro["titulo"]}" ha sido prestado.')
            else:
                print(f'El libro "{libro["titulo"]}" no está disponible para prestar.')
            return
    print(f'No se encontró el libro con el título "{titulo}".')


def mostrar_libros_disponibles():
    print("Libros disponibles:")
    for libro in libros:
        if libro["estado"] == "disponible":
            print(
                f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}"
            )
