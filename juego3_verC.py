import random
import json
import os
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
    Aquí te explico cómo funciona este juego. Vas a jugar contra el ordenador, por lo cual solo tenes que elegir 
    entre las 3 opciones: PIEDRA, PAPEL o TIJERA. Por cada acierto, ganarás un punto. Pero ¡ojo! Si te equivocas 3 veces, 
    el juego se termina. Al final del la partida, te mostraremos cuántos puntos conseguiste. 
    Recuerda ser preciso al responder, si eliges una opción incorrecta, te pediremos que elijas una válida.
    ¡Listo! ¡¡Buena suerte!!''' 
    print()
    print(Style.BRIGHT + f' Bienvenido al juego de PIEDRA, PAPEL o TIJERA '.center(60,'-'))
    print(texto)
    print('-'*60)

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

puntosTotal = 0

def piedra_papel_tijera(): #juego3 (la tercera es la venciada)
    global puntosTotal
    opc = ["PIEDRA","PAPEL","TIJERA"]
    opcU = ["PIEDRA","PAPEL","TIJERA"]
    puntos = 0
    errores = 0
    textoIntro()
    
    while True:
        opcUsuario = input("\n----> Ingrese su opcion: ").upper()

        if opcUsuario not in opc:
            print('\nOpcion invalida...')
            print(Back.YELLOW + Style.BRIGHT + 'Por favor SOLO ingrese una de estas opciones... >>   PIEDRA, PAPEL o TIJERA')
            continue
        opcPc = random.choice(opcU)
        print(f"\nLa PC ha elegido: {opcPc}")
        if opcUsuario == opcPc:
            print(f"\nHan empatado, ambos eligieron {opcUsuario}")
        elif opcUsuario == "PIEDRA" and opcPc == "TIJERA":
            print(Fore.GREEN + f"\nGanaste!, {opcUsuario} gana contra {opcPc}")
            puntos += 1
            puntosTotal += 1
        elif opcUsuario == "TIJERA" and opcPc == "PAPEL":
            print(Fore.GREEN + f"\nGanaste!, {opcUsuario} gana contra {opcPc}") 
            puntos += 1
            puntosTotal += 1
        elif opcUsuario == "PAPEL" and opcPc == "PIEDRA":
            print(Fore.GREEN + f"\nGanaste!, {opcUsuario} gana contra {opcPc}") 
            puntos += 1
            puntosTotal += 1
        else:
            print()
            print(Fore.RED + f"Perdiste, {opcUsuario} pierde contra {opcPc}")
            errores += 1
            if errores == 3:
                print(Fore.CYAN + f"Has alcanzado el límite de 3 equivocaciones... Fin de la partida!\n")
                print(f"Felicitaciones!!! En total obtuviste: {puntos} puntos en esta partida.\n")
                ## Seguir...
                break

    seguir = input(Style.BRIGHT + "¿Quieres jugar nuevamente? (S/N) -> ")
    if seguir.upper() == 'S':
        limpiar()
        piedra_papel_tijera()
    else:
        print()
        print(Style.BRIGHT + f'Total de puntos obtenidos: {puntosTotal} puntos.')
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

############### Principal ##############################3 

piedra_papel_tijera()
