# Ingresar la edad de una persona y decir si puede entrar a un evento (solo mayores de 18 años).

print('INGRESE SU EDAD:')
edad = int(input())
if edad >= 18:
    print('Usted puede entrar al evento.')
else:
    print('Usted no puede entrar al evento.')
