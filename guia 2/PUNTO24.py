# Permitir ingresar datos de varios empleados (nombre, sector, sueldo base, antigüedad). Calcular el sueldo final según el siguiente criterio:
# ● Antigüedad < 5 años → +5%.
# ● Antigüedad entre 5 y 10 → +10%.
# ● Antigüedad > 10 → +20%.
# ● Mostrar un informe con el sueldo final de cada empleado y el
# promedio general.

empleados = []


def agregar_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    sector = input("Ingrese el sector del empleado: ")
    sueldo_base = float(input("Ingrese el sueldo base del empleado: "))
    antiguedad = int(input("Ingrese la antigüedad del empleado (en años): "))
    empleado = {
        "nombre": nombre,
        "sector": sector,
        "sueldo_base": sueldo_base,
        "antiguedad": antiguedad,
    }
    empleados.append(empleado)


def sueldo_final_especifico():
    nombre = input("Ingrese el nombre del empleado del que quiere calcular su sueldo: ")
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre.lower():
            return calcular_sueldo_final(empleado)
    return None


def calcular_sueldo_final(empleado):
    antiguedad = empleado["antiguedad"]
    if antiguedad < 5:
        porcentaje = 0.05
    elif antiguedad <= 10:
        porcentaje = 0.10
    else:
        porcentaje = 0.20
    return empleado["sueldo_base"] * (1 + porcentaje)


def mostrar_informe():
    if not empleados:
        print("No hay empleados cargados.")
        return

    total_sueldos = 0
    print("\nInforme de sueldos:")
    for empleado in empleados:
        sueldo_final = calcular_sueldo_final(empleado)
        total_sueldos += sueldo_final
        print(f"{empleado['nombre']} ({empleado['sector']}): ${sueldo_final:.2f}")

    promedio = total_sueldos / len(empleados)
    print(f"Promedio general: ${promedio:.2f}")


def main():
    cantidad = int(input("Ingrese la cantidad de empleados: "))
    for _ in range(cantidad):
        agregar_empleado()

    mostrar_informe()
    nombre = input("Ingrese el nombre de un empleado para consultar su sueldo (o Enter para omitir): ")
    if nombre:
        sueldo_final = sueldo_final_especifico_por_nombre(nombre)
        if sueldo_final is None:
            print("No se encontró ese empleado.")
        else:
            print(f"Sueldo final de {nombre}: ${sueldo_final:.2f}")


def sueldo_final_especifico_por_nombre(nombre):
    for empleado in empleados:
        if empleado["nombre"].lower() == nombre.lower():
            return calcular_sueldo_final(empleado)
    return None


if __name__ == "__main__":
    main()
