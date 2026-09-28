# Ingresar la base y la altura de un rectángulo, calcular el área y el perímetro.

print('INGRESE LA BASE DEL RECTÁNGULO:')
base = float(input())
print('INGRESE LA ALTURA DEL RECTÁNGULO:')
altura = float(input())
area = base * altura
perimetro = 2 * (base + altura)
print(f'El área del rectángulo es: {area}')
print(f'El perímetro del rectángulo es: {perimetro}')
