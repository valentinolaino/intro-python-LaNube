# Pedir dos números y una operación (+, -, *, /) y mostrar el resultado.
print('INGRESE EL PRIMER NÚMERO:')
num1 = float(input())
print('INGRESE EL SEGUNDO NÚMERO:')
num2 = float(input())
print('INGRESE LA OPERACIÓN (+, -, *, /):')
operacion = input()
if operacion == '+':
      resultado = num1 + num2
      print(f'El resultado de {num1} + {num2} es: {resultado}')
elif operacion == '-':
      resultado = num1 - num2
      print(f'El resultado de {num1} - {num2} es: {resultado}')
elif operacion == '*':
      resultado = num1 * num2
      print(f'El resultado de {num1} * {num2} es: {resultado}')
elif operacion == '/':
      if num2 != 0:
            resultado = num1 / num2
            print(f'El resultado de {num1} / {num2} es: {resultado}')
      else:
            print('Error: No se puede dividir entre cero.')
            