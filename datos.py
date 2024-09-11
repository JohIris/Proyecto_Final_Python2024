## Datos almacenados de los usuarios...
import json
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Creamos el archivo json con los datos de los usuarios ya alcenados...
ruta = 'datosVarios/'
nombreArchivo = 'datosUsua.json'

usuarios = [
    {
        'alias': 'JOHA',
        'clave': 'jh89',
        'nombre': 'Johanna',
        'puntos': 100
    },
    {
        'alias': 'SEBA',
        'clave': 'sb88',
        'nombre': 'Sebastian',
        'puntos': 100
    },
    {
        'alias': 'CAMI',
        'clave': 'cm91',
        'nombre': 'Camila',
        'puntos': 100
    },
    {
        'alias': 'RODRI',
        'clave': 'rd90',
        'nombre': 'Rodrigo',
        'puntos': 100
    },
    {
        'alias': 'JESI',
        'clave': 'js92',
        'nombre': 'Jessica',
        'puntos': 100
    },
    {
        'alias': 'NADU',
        'clave': 'nd87',
        'nombre': 'Nadia',
        'puntos': 100
    },
    {
        'alias': 'MAKI',
        'clave': 'mc93',
        'nombre': 'Macarena',
        'puntos': 100
    }
]

with open(ruta+nombreArchivo,'w') as info:
    json.dump(usuarios,info,indent=2)

print('')
print(Back.GREEN + 'El archivo fue creado con exito...!')