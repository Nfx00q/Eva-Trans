import time
import numpy as np
from entities import *
from funcs import *

arreglo_concierto = np.full((10, 10), '----')
lista_usuario = []

def salir():
    print("Cerrando entorno (By Benjamin Belmar V1.0)")
    time.sleep(2)
    return False

llenar_arreglo(arreglo_concierto)

ciclo = True
while ciclo:
    print("1) Comprar entradas.")
    print("2) Mostrar ubicaciones disponibles.")
    print("3) Ver listado de asistentes.")
    print("4) Ganancias totales.")
    print("5) Salir.")
    try:
        op_menu = int(input("> Inserte una opción entre 1 y 5 -> "))
        match op_menu:
            case 1:
                print("--- Compra de entradas ---")
                comprar_entrada(arreglo_concierto, lista_usuario)
            case 2:
                print("------------ Ubicaciones disponibles -------------")
                mostrar_arreglo(arreglo_concierto)
            case 3:
                print("--- Listado de asistentes ---")
                listar_usuarios(lista_usuario)
            case 4:
                print("--- Ganancias totales ---")
                num_as = 0
                total(arreglo_concierto)
            case 5:
                ciclo = salir()
            case _:
                print("!- Error, opción ingresada no es valida.")
                time.sleep(2)
    except BaseException as error:
        print(f"Error code -> {error}")
