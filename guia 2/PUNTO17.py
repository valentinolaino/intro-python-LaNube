# Permitir ingresar varios contactos con nombre, teléfono y email. Buscar un contacto por nombre y mostrar sus datos.
contactos = [
    {"nombre": "Juan", "telefono": "123456789", "email": "juan@email.com"},
    {"nombre": "Lucas", "telefono": "11111111", "email": "lucas@email.com"},
    {"nombre": "Pedro", "telefono": "987654321", "email": "pedro@email.com"},
]

buscado = input("Ingrese el nombre del contacto a buscar: ")
for contacto in contactos:
    if contacto["nombre"] == buscado:
        print("El nombre fue encontrado con éxito, :")
        print(f"Nombre: {contacto['nombre']}")
        print(f"Telefono: {contacto['telefono']}")
        print(f"Email: {contacto['email']}")
    else:
        print("Contacto no encontrado.")
        break
