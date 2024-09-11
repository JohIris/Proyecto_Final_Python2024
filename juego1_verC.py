#version mejorada del ahorcado. 
import random
import datosVarios.listaNivel as listaNivel
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
    El juego consiste en adivinar la Palabra Secreta que aparecerá en pantalla. Tenemos disponibles 3 niveles de dificultad, 
    para que escojas el que gustes. Si ganas, te preguntaremos si queres seguir jugando. Recorda escoger sabiamente cada 
    letra que vas a usar, porque solo te podrás equivocar 6 veces en cada partida. Si perdes, el juego se acaba. 
    Buena suerte!! 
    ''' 
    print()
    print(Style.BRIGHT + f" Bienvenido al juego del AHORCADO ".center(50,"-"))
    print(texto)

def niveles():
  print("-"*40)
  print(Style.BRIGHT + Fore.GREEN + "NIVELES DE DIFICULTAD".center(40))
  print("-"*40)
  print("1.   FÁCIL")
  print("2.   MEDIO")
  print("3.   DIFÍCIL")
  print("0.   SALIR")
  print("-"*40)

def palabraSecreta():
  while True:
    niveles()
    opcion = input("Ingresa el número de la dificultad: ")
    match opcion:
      case "1":
        return random.choice(listaNivel.facil).upper()
      case "2":
        return random.choice(listaNivel.medio).upper()
      case "3":
        return random.choice(listaNivel.dificil).upper()
      case "0":
        print(Back.LIGHTWHITE_EX + "Fin del juego")
        print()
        volverPrincipal()
        break
      case _:
        print(Fore.RED + "Opción inválida. Por favor, volve a intentarlo.")


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
    else:
      viejosPuntos = usuario['puntos']
      nuevosPuntos = viejosPuntos + 1
      usuario['puntos'] = nuevosPuntos
      print(f"Los puntos de {aliasDado} se actualizaron con éxito")
      with open(ruta+nombreArchivo,"w+") as infoN:
        json.dump(losDatosG,infoN,indent=2)
    input("\nPresione una tecla para continuar...")
    limpiar()
    break

##  -------->>      Para buscar los datos de los alumnos
def buscar_usuario(alias):
    for dato in losDatosG:
        if alias in dato['alias']:
            return dato
    return None


def ahorcado(): #JUEGO 1
  while True:
    textoIntro()
    palabra = palabraSecreta()
    letrasAdi = []
    vidas = 6
    letrasUsa = []

    while len(palabra) > 0 and vidas > 0:
      auxiliar = [letter if letter in letrasUsa else "_" for letter in palabra]
      print(f"\nIntenta adivinar esta palabra:", " ".join(auxiliar))

      letra = input("Ingresa una letra: ").upper()
      if len(letra) != 1 or not letra.isalpha():
        print(Fore.RED + "Opcion Invalida!! Por favor ingresa SOLO UNA letra.")
        continue
      if letra in letrasUsa:
        print(f"Ya has usado esta letra {letra}. Intenta con otra distinta.")
        continue

      letrasUsa.append(letra)
      if letra in palabra:
        print(Fore.GREEN + "¡Acertaste!")
        letrasAdi.append(letra)
        if set(letrasAdi) == set(palabra):
          print("\n¡Ganaste! La palabra secreta era:", palabra)
          ##Cuando ganas... 
          respuesta = input(Style.BRIGHT + "¿Quieres jugar nuevamente? (S/N) -> ")
          if respuesta.upper() == "S":
            guardarPuntos()
            break
          else:
            guardarPuntos()
            volverPrincipal()
            break
          
      else:
        vidas -= 1
        print(Fore.LIGHTRED_EX + f"¡Fallaste! La letra {letra} no pertenece a la palabra.")
        print("Ya usaste las letras:"," - ".join(letrasUsa))
        print(Back.YELLOW + f"Te quedan vidas {vidas} restantes.")

    if vidas == 0:
      print(Back.LIGHTRED_EX + f"Perdiste... La palabra era: {palabra}")
      print("¡Gracias por jugar!\n") 
      respuesta = input(Style.BRIGHT + "¿Quieres jugar nuevamente? (S/N) -> ")
      if respuesta.upper() == "S":
        continue
      else:
        break
  limpiar()

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
  

#################### Programa principal
ahorcado()