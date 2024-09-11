# Menor-Mayo-Igual
import os
import json
import random
from colorama import Fore, Back, Style, init
init(autoreset=True)

ruta = 'datosVarios/'
nombreArchivo = 'datosUsua.json'
##########################################################

## ------------->>   Obtner los datos de los usuarios almacenados...
with open(ruta+nombreArchivo) as infoG:
    losDatosG = json.load(infoG)

def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def textoIntro():
    texto ='''
    Aquí te explico cómo funciona este juego. Al inicio, se te mostrará en pantalla un número al azar del 1 al 100 
    y tendrás que adivinar si el siguiente número será Mayor, Menor o Igual que el anterior. Por cada respuesta correcta, 
    ganarás un punto, pero ¡ojo! Si te equivocas, se termina la partida. Al finalizar, te mostraremos cuántos puntos conseguiste.
    Recuerda ser preciso al responder, si eliges una opción incorrecta, te pediremos que elijas una válida.
    ¡Listo! ¡¡Buena suerte!!''' 
    print()
    print(Style.BRIGHT + f' Bienvenidos al juego: MAYOR-MENOR-IGUAL '.center(80,'-'))
    print(texto)
    print('-'*80)

##   --------->>      Guardar puntos en el archivo json
def guardarPuntos():
  global puntos
  print()
  print("Guardando sus datos...\n")
  while True:
    aliasDado = input("Reingrese su Usuario: ").upper()
    usuario = buscar_usuario(aliasDado)
    if usuario is None:
      print(Fore.LIGHTRED_EX + f"El Usuario {aliasDado} no esta registrado!!")
      print("Por favor, ingrese un Usuario valido") ##arreglando esto
      continue
    else:
      viejosPuntos = usuario['puntos']
      nuevosPuntos = viejosPuntos + puntosTotal
      usuario['puntos'] = nuevosPuntos
      print(f"Los puntos de {aliasDado} se actualizaron con éxito")
      with open(ruta+nombreArchivo,"w+") as infoN:
        json.dump(losDatosG,infoN,indent=2)

    break

##  -------->>      Para buscar los datos de los alumnos
def buscar_usuario(alias):
    for dato in losDatosG:
        if alias in dato['alias']:
            return dato
    return None

def ronda(numAzar):
    while True:
        respuesta = input(f'\n¿El próximo número que aparecerá es Mayor, Menor o Igual? ')
        respuesta = respuesta.upper()
        if respuesta not in ['MAYOR', 'MENOR', 'IGUAL']:
            print(Fore.YELLOW + 'Opcion no valida. Intente nuevamente.')
            continue
        numSecreto = random.randint(1, 100)
        match respuesta:
            case 'MAYOR':
                if numSecreto > numAzar:
                    print(Fore.GREEN + f'Muy bien!!  El número es: {numSecreto}')
                    return True, numSecreto
                else:
                    print(Fore.RED + f'\nPerdiste. El número es: {numSecreto}')
                    return False, None
            case 'MENOR':
                if numSecreto < numAzar:
                    print(Fore.GREEN + f'Muy bien!!  El número es: {numSecreto}')
                    return True, numSecreto
                else:
                    print(Fore.RED + f'\nPerdiste. El número es: {numSecreto}')
                    return False, None
            case 'IGUAL':
                if numSecreto == numAzar:
                    print(Fore.GREEN + f'Muy bien!!  El número es: {numSecreto}')
                    return True, numSecreto
                else:
                    print(Fore.RED + f'\nPerdiste. El número es: {numSecreto}')
                    return False, None
                
puntosTotal = 0

def adivinar():
    global puntosTotal
    textoIntro()
    puntaje = 0
    numAzar = random.randint(1, 100)
    print()
    print(Fore.CYAN + Style.BRIGHT + f'Empezamos el juego con este número: {numAzar}')

    while True:
        avanzar, numAzar = ronda(numAzar)
        if avanzar:
            puntaje += 1
            puntosTotal += 1
        else:
            print(f' Fin de la partida! '.center(60, '~'))
            break
    print(f'En total obtuviste: {puntaje} puntos en esta ronda.\n')
    seguir = input(Style.BRIGHT + "¿Quieres jugar nuevamente? (S/N) -> ")
    if seguir.upper() == "S":
        limpiar()
        adivinar()
    else:
        print(Style.BRIGHT + Back.CYAN + f'Total de puntos obtenidos: {puntosTotal} puntos.')
        guardarPuntos()
        print()
        print(Back.LIGHTWHITE_EX + " Fin del juego ".center(60, '~'))
        print()
        volverPrincipal()

def volverPrincipal():
    while True:
        rta = input(Style.BRIGHT + "¿Queres volver al MENU DE USUARIOS? (S/N) -> ")
        if rta.upper() == "S":
            limpiar()
            from principal_verC import principal
            break
        else:
            limpiar()
            break


######### Progrma Principal
adivinar()