from pprint import pprint

ciudades = [
    {
        'nombre':'Tumbes',
        'habitantes': 500000
    },
    {
        'nombre':'Arequipa',
        'habitantes': 800000  
    },
    {
        'nombre':'Loreto',
        'habitantes': 100000
    }
]

def miFuncion(ciudad):
    return ciudad['habitantes']

ciudades.sort(key=miFuncion)
# pprint(ciudades)

ciudades.append({'nombre':'Cusco','habitantes': 20000})
# pprint(ciudades)

lista = ['Arequipa','Cusco','Tumbes']
lista.remove('Arequipa')
pprint(lista)


