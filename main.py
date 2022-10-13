from Ejercicio_1 import Ejercicio11,Ejercicio12
from Ejercicio_2 import Ejercicio21,Ejercicio22
from Ejercicio_3 import Ejercicio31,Ejercicio32
#from Ejercicio_4 import Ejercicio41,Ejercicio42,Ejercicio43
import os
import platform
'''Ejercicio11.Ejercicio11.ejecutar()
Ejercicio12.Ejercicio12.ejecutar()
Ejercicio21.Ejercicio21.ejecutar()
Ejercicio22.Ejercicio22.ejecutar()
Ejercicio31.Ejercicio31.ejecutar()
Ejercicio32.Ejercicio32.ejecutar()
#Ejercicio41.Ejercicio41.ejecutar()
#Ejercicio42.Ejercicio42.ejecutar()
#Ejercicio43.Ejercicio43.ejecutar()
#Ejercicio44.Ejercicio44.ejecutar()'''

def limpiar_pantalla():
    os.system('cls') if platform.system()=='Windows' else os.system('clear')
def iniciar():
    while True:
        limpiar_pantalla()

        print("========================")
        print("  Bienvenid@ a la resolución de los ejercicios  ")
        print("========================")
        print("[1] Ejercicio 1 ")
        print("[2] Ejercicio 2 ")
        print("[3] Ejercicio 3 ")
        print("[4] Ejercicio 4 ")
        print("========================")

        opcion = input("> ")
        limpiar_pantalla()

        if opcion == '1':
            print("Ejercicio 1.1: ")
            Ejercicio11.Ejercicio11.ejecutar()
            print("========================")
            print("Ejercicio 1.2: ")
            Ejercicio12.Ejercicio12.ejecutar()

        elif opcion == '2':
            print("Ejercicio 2.1: ")
            Ejercicio21.Ejercicio21.ejecutar()
            print("========================")
            print("Ejercicio 2.2: ")
            Ejercicio22.Ejercicio22.ejecutar()

        elif opcion == '3':
            print("Ejercicio 3.1: ")
            Ejercicio31.Ejercicio31.ejecutar()
            print("========================")
            print("Ejercicio 3.2: ")
            Ejercicio32.Ejercicio32.ejecutar()

        elif opcion == '4':
            print("Ejercicio 4.1: ")
            #Ejercicio41.Ejercicio41.ejecutar()
            print("========================")
            print("Ejercicio 4.2: ")
            #Ejercicio42.Ejercicio42.ejecutar()
            print("========================")
            print("Ejercicio 4.3: ")
            #Ejercicio43.Ejercicio43.ejecutar()
            print("========================")
            print("Ejercicio 4.4: ")
            #Ejercicio44.Ejercicio44.ejecutar()
            print("prueba")
        input("\nPresiona ENTER para continuar...")


if __name__=="__main__":
    iniciar()