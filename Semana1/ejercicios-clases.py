from pprint import pprint

# Crear una clase operaciones y con sus respectivos metodos (sumar, restar, multiplicar, dividir)
class Operaciones:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
        
    def metodoSumar(self):
        resultado = self.num1 + self.num2
        return f'La suma de los dos numeros ingresados es : {self.__redondear(resultado)}'
    
    def metodoRestar(self):
        resultado = self.num1 - self.num2
        return f'La resta de los dos numeros ingresados es : {self.__redondear(resultado)}'
    
    def metodoMultiplicar(self):
        resultado = self.num1 * self.num2
        return f'La multiplicacion de los dos numeros ingresados es : {self.__redondear(resultado)}'
    
    def metodoDividir(self):
        resultado = self.num1 / self.num2
        return f'La division de los dos numeros ingresados es : {self.__redondear(resultado)}'
    
    def __redondear(self, numero):
        return round(numero , 2)


    
x = Operaciones(7, 3)
# print(x.metodoSumar())
# print(x.metodoRestar())
# print(x.metodoDividir())
# print(x.metodoMultiplicar())

# Crear una clase de un Usuario que reciba (nombre,edad,dni,estatura,estado_civil) y crear un metodo que nos convierta estos datos en un diccionario

class Usuario:
    def __init__(self, nombre, edad ,dni ,estatura ,estado_civil) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.estatura = estatura
        self.estado_civil = estado_civil

    def convertidorDiccionario(self):
        return {
            'nombre': self.nombre,
            'edad':self.edad,
            'dni':self.dni,
            'estatura':self.estatura,
            'estado_civil':self.estado_civil
        }

        # usuario.append({'nombre':{self.nombre},'edad':{self.edad},'dni':{self.dni},'estatura':{self.estatura},'estado_civil':{self.estado_civil}})

usuario = Usuario('Mateo Quispe Pacheco','25','73276257','1.70','comprometido')
pprint(usuario.convertidorDiccionario())











