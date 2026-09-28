# Pedir las notas de 10 alumnos y contar cuántos aprobaron (nota mayor o igual a 6).

print('INGRESE LAS NOTAS DE 10 ALUMNOS:')
notas = []
for i in range(10):
    print(f'INGRESE LA NOTA DEL ALUMNO {i + 1}:')
    nota = float(input())
    notas.append(nota)

aprobados = sum(1 for nota in notas if nota >= 6)
print(f'Cantidad de alumnos aprobados: {aprobados}')