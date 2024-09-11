#### Ingreso de los Usuarios...
import json
import os
from colorama import Fore, Back, Style, init
init(autoreset=True)

## (+) Obtner los datos de los usuarios almacenados...
ruta = 'datosVarios/'
nombreArchivo = 'datosUsua.json'

with open(ruta+nombreArchivo) as infoG:
    losDatosG = json.load(infoG)

def buscar_usuario(alias, dato):
    for dato in losDatosG:
        if alias == dato['alias']:
            return dato
    return None

##      >>>>>>>>      Funciones para ingresar al sistema
def validarIngreso(dato, alias, clave):
    if alias == dato['alias'] and clave == dato['clave']:
        return True
    return False

def ingresoUs():
    intentos = 3
    while intentos > 0:
        aliasIng = input('\nIngrese su nombre de usuario: ').upper()
        dato = buscar_usuario(aliasIng, losDatosG)
        if dato:
            claveIng = input('Ingrese su contraseña: ')
            if validarIngreso(dato, aliasIng, claveIng):
                limpiar()
                print(Back.GREEN + Style.BRIGHT + f"Hola {aliasIng} te damos la bienvenida a >>>> ARCADE 2024!!")
                from menu_verC import menuSistema
                return True
            else:
                print(Fore.LIGHTRED_EX + "Contraseña incorrecta...")
                intentos -= 1
                print(f"Te quedan {intentos} intentos")
                break
        else:
            print(Fore.LIGHTRED_EX + "Usuario incorrecto... Volve a intentarlo...")
            intentos -= 1
            print(f"Te quedan {intentos} intentos")

    print(Fore.LIGHTRED_EX + "Se han agotado los intentos...")
    input("\nPresione una tecla para continuar...")
    limpiar()
    
##      >>>>>>>>      Guarda los datos de los usuarios nuevos en el archivo json

def pedir_alias():
    return input("Ingresa un nombre de usuario: ").upper() 

def validar_alias(alias, dato):
    for dato in losDatosG:
        if alias == dato['alias']:
            return False
        return True

def nuevos_datos():
    nNombre = input("Ingrese su nombre: ").capitalize()
    nClave = input("Ingrese una contraseña: ")
    return nNombre, nClave

def crear_nuevoUs(alias, nombre, clave):
    nuevoUsua = {
        'alias': alias,
        'clave': clave,
        'nombre': nombre,
        'puntos': 0  
        }
    return nuevoUsua

def guardar_nuevoUs(usuario,ruta, nombreArchivo): ##usuario o dato
    with open(ruta+nombreArchivo,"w") as infoN:
        json.dump(losDatosG,infoN,indent=2)

def crearUs():
    nAlias = pedir_alias()
    if validar_alias(nAlias, losDatosG):
        nNombre, nClave = nuevos_datos()
        nuevoUsua = crear_nuevoUs(nAlias, nNombre, nClave)
        losDatosG.append(nuevoUsua)
        guardar_nuevoUs(nuevoUsua, ruta, nombreArchivo)
        print(Fore.GREEN + Style.BRIGHT +"\n El nuevo registro se guardo con exito!! ")
    else:
        print(Fore.RED + Style.BRIGHT +"\n Nombre de usuario ya esta registrado!! Intente con otro...")
        
    print()
    mostrarUs()
    input("\nPresione una tecla para continuar...")
    limpiar()

###     >>>>>>>>      Funciones para modficar datos de los usuarios

def modificar_usuario(usuario):
    aliasG = input("Nuevo Usuario: ").upper()
    nombreG = input("Nombre: ").capitalize()
    claveG = input("Contraseña: ")
    usuario['alias'] = aliasG
    usuario['nombre'] = nombreG
    usuario['clave'] = claveG
    print(Back.YELLOW + f"Los datos de {aliasG} se modificaron con éxito")
    #actlizar los datos de archivo json
    with open(ruta+nombreArchivo, "w") as infoM:
        json.dump(losDatosG, infoM, indent=2)
    print()

def modificarUs():
    while True:
        aliasDado = input("Ingrese el Usuario: ").upper()
        print()
        usuario = buscar_usuario(aliasDado)
        if usuario is None:
            print(Fore.LIGHTRED_EX + f"El Usuario {aliasDado} no esta registrado!!")
            print()
        else:
            modificar_usuario(usuario)
            break
    mostrarUs()
    input("\nPresione una tecla para continuar...")
    limpiar()
    
##      >>>>>>>>      Funciones para eliminar usuarios

##(+) Permite eliminar registros de os usuarios almacenados
def eliminarUs():
    print()
    usuario = input('Ingrese el Usuario que desea eliminar: ').upper()
    encontrado = False
    for dato in losDatosG:
        if usuario == dato['alias']:
            encontrado = True
            print(Fore.CYAN + f'Este Usuario corresponde a {dato['nombre']}\n')
            confirmacion = input(Style.BRIGHT + 'Estas seguro de borrar este Usuario? S/N ').upper()
            if confirmacion == "S":
                losDatosG.remove(dato)
                print()
                print(Back.LIGHTYELLOW_EX + f'El registro de {usuario} fue eliminado con exito')
                #actlizar los datos de archivo json
                with open(ruta+nombreArchivo, "w") as infoN:
                    json.dump(losDatosG, infoN, indent=2)
            else:
                print(Back.WHITE + "Operacion cancelada.")
            break
    if not encontrado:
        print(f'El Usuario {usuario} no esta registrado')
        print(Fore.LIGHTRED_EX + 'Operacion cancelada.')
    print()
    mostrarUs()
    input("\nPresione una tecla para continuar...")
    limpiar()
## (+)Para buscar los datos de algun usuario en particular
def buscarUs():
    print()
    aliasB = input('Ingrese el Usuario que desea buscar: ').upper()
    encontrado = False
    for dato in losDatosG:
        if aliasB == dato['alias']:
            print()
            print('-'*38)
            print(Style.BRIGHT + Fore.GREEN + '|  ALIAS  |    NOMBRE    |  PUNTAJE  |')
            print('|---------+--------------+-----------|')
            print(f'|{dato['alias']:^9}|', end='')
            print(f'{dato['nombre']:^14}|', end='')
            print(f'{dato['puntos']:^11}|')
            print('-'*38)
            encontrado = True
            break
    if not encontrado:
            print(Fore.LIGHTRED_EX + f'El Usuario {aliasB} no esta registrado en el sistema...!\n')
            opcion = input('¿Desea registrarlo en nuestro sistema? (S/N) ').upper()
            if opcion == 'S':
                print()
                crearUs()
            elif opcion == 'N':
                print(Fore.CYAN + 'Operacion cancelada.')
    input('Presione una tecla para continuar...')
    limpiar()
## (+)Muestra todos los datos de los usuarios alamacenados
def mostrarUs():
    print(Style.BRIGHT + Back.LIGHTWHITE_EX + 'LISTA DE USUARIOS'.center(40))
    print('|  ALIAS  |    NOMBRE    |  PUNTAJE  |')
    print('|---------+--------------+-----------|')
    for dato in losDatosG:
        print(f'|{dato['alias']:^9}|', end='')
        print(f'{dato['nombre']:^14}|', end='')
        print(f'{dato['puntos']:^11}|')
    print('-'*40)

## (+) Muestra los puntajes alamacenados de los jugadores 
def mostrarPuntaje():
    print()
    print(Style.BRIGHT + Back.LIGHTWHITE_EX + 'TABLA DE PUNTAJE'.center(23))
    print('|  ALIAS  |  PUNTAJE  |')
    print('|---------+-----------|')
    for dato in losDatosG:
        print(f'|{dato['alias']:^9}|', end='')
        print(f'{dato['puntos']:^11}|')
    print('-'*23)
    input('Presione una tecla para continuar...')
    limpiar()
## (+) funcion para limpiar la terminal. 
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
    #input('Presione una tecla para continuar...')
##########################################################
def principal():
    while True:
        print()
        print("-"*40)
        print(Style.BRIGHT + Back.LIGHTWHITE_EX + "MENÚ DEL USUARIO".center(40))
        print("-"*40)
        print("1.   INGRESAR ")
        print("2.   CREAR USUARIO")
        print("3.   MODIFICAR USUARIO")
        print("4.   ELIMINAR USUARIO")
        print("5.   BUSCAR USUARIO")
        print("6.   MOSTRAR TABLA DE PUNTUACIONES")
        print("0.   SALIR")
        print("-"*40)
        opcion = input("Ingrese opcion ---> ")

        match opcion:
            case "1":
                ingresoUs()
                pass
            case "2":
                crearUs()
                pass
            case "3":
                modificarUs()
            case "4":
                eliminarUs()
            case "5":
                buscarUs()
            case "6":
                mostrarPuntaje()
            case "0":
                print(Back.LIGHTWHITE_EX + Style.BRIGHT + "Fin del programa... Gracias por utilizar nuestro Programa...")
                print()
                break
            case _:
                print(Fore.LIGHTRED_EX + "Opcion no valida... Vuelve a intentarlo")
                input("\nPresione una tecla para continuar...")
                limpiar()
    #return False        

################## Programa Princpal

principal()

## ... >>>
#cuando vuelve al menu principal, desde algun juego... vuelve a mostar el menu principal
#y cuando hago el ingreso , no permite volver a ingresar al menu de los juegos.
# hay que salir dos veces del menu del usuario... y queda el mensaje de inciando el juego anterior... 
