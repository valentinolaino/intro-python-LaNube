# Desarrollar un programa que permita registrar gastos diarios (fecha, categoría y monto). El sistema debe:
# ● Permitir agregar nuevos gastos.
# ● Mostrar el total gastado en el mes.
# ● Mostrar el total por categoría.
# ● Calcular el promedio diario de gasto.

gastos = []


def agregar_gasto():
    fecha = input("Ingrese la fecha del gasto (YYYY-MM-DD): ")
    categoria = input("Ingrese la categoría del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))
    gasto = {"fecha": fecha, "categoria": categoria, "monto": monto}
    gastos.append(gasto)


def total_gastado(mes, año):
    total = 0
    for gasto in gastos:
        gasto_fecha = gasto["fecha"].split("-")
        gasto_año = int(gasto_fecha[0])
        gasto_mes = int(gasto_fecha[1])
        if gasto_año == año and gasto_mes == mes:
            total += gasto["monto"]
            return total


def total_categoria(categoria):
    total = 0
    for gasto in gastos:
        if gasto["categoria"].lower() == categoria.lower():
            total += gasto["monto"]
            return total


def promedio_diario(mes, año):
    total = total_gastado(mes, año)
    dias_en_mes = 30
    promedio = total / dias_en_mes
    return promedio
