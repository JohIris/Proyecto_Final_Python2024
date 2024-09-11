import os
import random
import json
from colorama import Fore, Back, Style, init
init(autoreset=True)


ruta = 'datosVarios/'
nombreArchivo = 'datosUsua.json'

## ------------->>   Obtner los datos de los usuarios almacenados...
with open(ruta+nombreArchivo) as infoG:
    losDatosG = json.load(infoG)


def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def introJuego():
    intro = '''
Te explico el funcionamiento y de que trata este juego... 
Es un juego de estrategia simple para dos jugadores que se juega en una cuadrícula de 3x3. Se le asignará a cada jugador un símbolo, 
sea "X" o "O", y se turnan para colocarlo en una casilla vacía. 
El objetivo es ser el primero en alinear tres de sus símbolos de manera horizontal, vertical o diagonal. 
Si todas las casillas se llenan y ningún jugador logra alinear tres símbolos, el juego termina en empate. 
Para el llenado de las casillas, consiste en el siguiente orden:

          7 |  8  | 9 
        -  +  -  +  -
          4 |  5  | 6
        -  +  -  +  -
          1 |  2  | 3

Cada número representa la ubicación del símbolo a jugar.
Buena suerte!!!
    '''
    print()
    print("-" * 100)
    print(Style.BRIGHT + "Bienvenido al juego del Ta-Te-Ti!!".center(100))
    print(intro)
    print("-" * 100)

def imprimir_tablero(tablero):
    for fila in tablero:
        for i in range(len(fila)):
            if i == len(fila) - 1:
                print(fila[i], end='\n')
            else:
                print(fila[i], end='  ')

def cambiar_tablero(tablero, posicion, jugador):
    simbolo = 'x' if jugador else 'o'
    
    posiciones = {
        1: (4, 0), 2: (4, 2), 3: (4, 4),
        4: (2, 0), 5: (2, 2), 6: (2, 4),
        7: (0, 0), 8: (0, 2), 9: (0, 4)
    }
    
    fila, columna = posiciones.get(posicion, (None, None))
    
    if fila is not None and columna is not None and tablero[fila][columna] == ' ':
        tablero[fila][columna] = simbolo
        return 0
    else:
        return 'Esa posición ya está ocupada o no existe.'

def hay_ganador(tablero):
    for simbolo in ['x', 'o']:
        fila_0 = tablero[0][0] == simbolo and tablero[0][2] == simbolo and tablero[0][4] == simbolo
        fila_2 = tablero[2][0] == simbolo and tablero[2][2] == simbolo and tablero[2][4] == simbolo
        fila_4 = tablero[4][0] == simbolo and tablero[4][2] == simbolo and tablero[4][4] == simbolo
        columna_0 = tablero[0][0] == simbolo and tablero[2][0] == simbolo and tablero[4][0] == simbolo
        columna_2 = tablero[0][2] == simbolo and tablero[2][2] == simbolo and tablero[4][2] == simbolo
        columna_4 = tablero[0][4] == simbolo and tablero[2][4] == simbolo and tablero[4][4] == simbolo
        diagonal_abajo = tablero[0][0] == simbolo and tablero[2][2] == simbolo and tablero[4][4] == simbolo
        diagonal_arriba = tablero[4][0] == simbolo and tablero[2][2] == simbolo and tablero[0][4] == simbolo

        if fila_0 or fila_2 or fila_4 or columna_0 or columna_2 or columna_4 or diagonal_abajo or diagonal_arriba:
            if simbolo== "x":
                return 1
            else: 
                return 2 


def movimiento_maquina(tablero):
    posiciones = {
        1: (4, 0), 2: (4, 2), 3: (4, 4), #filas
        4: (2, 0), 5: (2, 2), 6: (2, 4),
        7: (0, 0), 8: (0, 2), 9: (0, 4)
    }      #columnas
    movimientos_validos = [] #creo una lista de movimientos validos
    for i in range(1, 10):
        fila, columna = posiciones[i]
        if tablero[fila][columna] == ' ': #se verifica que la casilla esté vacía
            movimientos_validos.append(i) #se agrega a la lista de movimientos permitidos
    if movimientos_validos:
        return random.choice(movimientos_validos) #devuelvo un valor aleatorio de los movimientos permitidos 
    return None

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


#### Programa Principal

jugador_1 = ''
victorias1 = 0 #del jugador
victorias2 = 0

while True:
    tablero = [
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' ']
    ]
    turno_1 = True
    turno = 0

    introJuego()
    if jugador_1 == '':
        jugador_1 = input("Nombre de jugador (x): ").upper()
    imprimir_tablero(tablero)
                
    while turno < 9:
        if turno_1:
            print()
            jugada = input(f"{jugador_1}, elige una posición: ")
            if jugada.isdigit():
                jugada = int(jugada)
                if jugada < 1 or jugada > 9:
                    print(Fore.YELLOW + "Elegí un número entre 1 y 9.")
                    continue
        else:
            jugada = movimiento_maquina(tablero)
            if jugada is None:
                print("Empate...")
                break
            print()
            print(Fore.CYAN + f"La máquina ha elegido la posición {jugada}")

        valor = cambiar_tablero(tablero, jugada, turno_1)
        if valor == 0:
            turno_1 = not turno_1
            turno += 1
            imprimir_tablero(tablero)
            ganador = hay_ganador(tablero)
            if ganador == 1:
                print(Fore.GREEN + Style.BRIGHT + f"Felicidades... {jugador_1} Ganaste!! ")
                victorias1 += 1 
                guardarPuntos()  
                break
            elif ganador == 2:
                print(Fore.RED + "Perdiste!! La máquina te ganó!")
                print() 
                # victorias2 += 1

                break
        else:
            if turno_1:
                print(valor)

        if turno == 9:
            print("Empate...")

    continuarJuego = input("¿Quieres volver a jugar? (S/N) ----> ").upper()
    if continuarJuego == "S":
        continue
    else:
        print(Style.BRIGHT + Back.WHITE + "Gracias por jugar! Hasta luego.")
        print()
        print("-" * 50)
        volverPrincipal()
        break
        