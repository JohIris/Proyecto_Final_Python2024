import os
from colorama import Fore, Back, Style, init
init(autoreset=True)

def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

##(+) funcion para jugar al ahorcado varias veces
def iniciarJuego1():
    print("Iniciando el juego del Ahorcado...\n")
    input(Fore.CYAN + "Presione una tecla para continuar...")
    while True:
        limpiar()
        from juego1_verC import ahorcado
        input("\nPresione una tecla para continuar...")

##(+) funcion para jugar al ahorcado varias veces
def iniciarJuego2():
    print("Iniciando el juego de MAYOR-MENOR-IGUAL...\n")
    input(Fore.CYAN + "Presione una tecla para continuar...")
    while True:
        limpiar()
        from juego2_verC import adivinar


def iniciarJuego3():
    print("Inicando el juego de PIEDRA-PAPEL-TIJERA...\n")
    input(Fore.CYAN + "Presione una tecla para continuar...")
    while True:
        limpiar()
        from juego3_verC import piedra_papel_tijera


def iniciarJuego4():
    while True:
        print("Iniciando el juego de TA-TE-TI...\n")
        input(Fore.CYAN + "Presione una tecla para continuar...")
        while True:
            limpiar()
            import taTeTi_verC as taTeTi_verC
        

def menuSistema():
    while True:
        print()
        print("-"*40)
        print(Style.BRIGHT + Back.LIGHTWHITE_EX + "LISTA DE JUEGOS:".center(40))
        print("-"*40)
        print(" 1.    AHORCADO")
        print(" 2.    MAYOR - MENOR - IGUAL")
        print(" 3.    PIEDRA, PAPEL o TIJERA")
        print(" 4.    TA - TE - TI")
        print(" 0.    Salir")
        print("-"*40)
        opcion = input("Elija un juego ---> ")
        match opcion:
            case '1':
                iniciarJuego1()
            case '2':
                iniciarJuego2()
            case '3':
                iniciarJuego3()
            case '4':
                iniciarJuego4()
            case '0':
                print(Back.LIGHTYELLOW_EX + "Saliendo del programa... Gracias por jugar con nocotros!")
                print()
                volverPrincipal()
                break
            case _:
                print(Fore.LIGHTRED_EX + "\nOpcion incorrecta! Por favor ingresa una opcion valida.")
        print()
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

############ Progrma Principal

menuSistema()
