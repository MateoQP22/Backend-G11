def suma(numero_1,numero_2):
    return numero_1+numero_2

def resta(numero_1,numero_2):
    return numero_1-numero_2

def division(numero_1,numero_2):
    return numero_1/numero_2

def multiplicacion(numero_1,numero_2):
    return numero_1*numero_2

operacion = input('Ingresa el tipo de operacion: ')
a = int(input('Ingresa el numero 1: '))
b = int(input('Ingresa el numero 2: '))


if operacion == 'S':
    resultado = suma(a,b)
elif operacion == 'R':
    resultado = resta(a,b)
elif operacion == 'D':
    resultado = division(a,b)
else:
    resultado = multiplicacion(a,b)

print(resultado)


# resultado_suma = suma(2,6)
# print(resultado_suma)


# resultado_resta = resta(10,4)
# print(resultado_resta)

# def estadoCivil(estado):
#     if(estado == 'soltero'):
#         print('soltero')
#     elif(estado == 'casado'):
#         print('casado')
#     else:
#         print('solo pipipii')

# estadoCivil('solo')


