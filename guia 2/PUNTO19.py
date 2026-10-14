# Ingresar una lista de jugadores con nombre y puntaje. Ordenar la lista de mayor a menor puntaje y mostrar el podio (los 3 primeros).

jugadores = [
    {"nombre": "Juan", "puntaje": 50},
    {"nombre": "Lucas", "puntaje": 510},
    {"nombre": "Roxana", "puntaje": 0},
    {"nombre": "María", "puntaje": 100},
]


print("Podio:")
jugadores.sort(key=lambda x: x["puntaje"], reverse=True)
for i, jugador in enumerate(jugadores[:3]):
    print(f"{i + 1}. {jugador['nombre']}: {jugador['puntaje']}")
