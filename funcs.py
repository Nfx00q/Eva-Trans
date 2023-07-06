import time
import numpy as np
import entities

def validar_rut():
    rut = int(input("> Ingrese su RUT (Sin puntos ni guión) -> "))
    if len(str(rut)) == 8:
        return rut
    else:
        print("RUT Ingresado incorrectamente.")
        time.sleep(2)
def llenar_arreglo(arreglo_concierto):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            arreglo_concierto[f][c] = str(x)

def mostrar_arreglo(arreglo_concierto):
    for f in range(10):
        fila = ''
        for c in range(10):
            dato = str(arreglo_concierto[f][c])
            if len(str(arreglo_concierto[f][c])) == 1:
                dato = '0' + str(arreglo_concierto[f][c])
            fila = fila + ' | ' + dato
        print(fila)

def validar_asiento():
    ciclo = True
    while (ciclo):
        try:
            asiento = int(input("> Ingrese el numero de asiento -> "))
            if asiento >= 1 and asiento < 101:
                return asiento
            else:
                print("!- Numero de asiento invalido o no disponible.")
        except BaseException as error:
            print(f"Error code -> {error}")

def validar_dis(arreglo_concierto, num_as):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if x == int(num_as):
                if str(arreglo_concierto[f][c]) == x:
                    return False
                else:
                    return True

def validar_opc():
    ciclo = True
    while(ciclo):
        try:
            can_as = int(input("> Indique la cantidad de asientos a comprar -> "))
            if can_as >= 1 and can_as <= 3:
                return can_as
            else:
                print("!- Cantidad de asientos incorrecta (Entre 1 y 3)")
        except BaseException as error:
            print(f"Error code -> {error}")
def comprar_entrada(arreglo_concierto, lista_usuario):
    can_as = validar_opc()
    x = 1
    while(x <= can_as):
        mostrar_arreglo(arreglo_concierto)
        print(f"> Seleccione el asiento deseado (N°{x}) -> ")
        num_as = validar_asiento()
        dis = validar_dis(arreglo_concierto, num_as)
        if dis:
            us = entities.Usuario()
            us.rut_us = validar_rut()
            marcar_asiento(arreglo_concierto, num_as)
            x = x + 1
            lista_usuario.append(us)
        else:
            print("!- Asiento no disponible, seleccione otro.")


def marcar_asiento(arreglo_concierto, num_as):
    x = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if x == int(num_as):
                arreglo_concierto[f][c] = 'XX'

def tipo_asiento(num_as):
    if num_as >= 1 and num_as <= 20:
        return 120000
    if num_as >= 21 and num_as <= 50:
        return 80000
    if num_as >= 51 and num_as <= 100:
        return 50000

def listar_usuarios(lista_usuario):
    x = 0
    for item in lista_usuario:
        x = x + 1
        print(f"ID: {x}\tRut: {str(item.rut_us)}")
        print("- - - - - - - - - - - - - - - - - -")

def contar(inicio, fin, arreglo_concierto):
    x = 0
    contador = 0
    for f in range(10):
        for c in range(10):
            x = x + 1
            if x >= inicio and x <= fin:
                if arreglo_concierto[f][c] == 'XX':
                    contador = contador + 1
    return contador

def total(arreglo_concierto):
    cant_plati = contar(1, 20, arreglo_concierto)
    cant_gold = contar(21, 50, arreglo_concierto)
    cant_silver = contar(51, 100, arreglo_concierto)

    plati = 120000 * cant_plati
    gold = 80000 * cant_gold
    silver = 50000 * cant_silver

    print(f"Entradas Platinium:\t ${plati}\t Cantidad: {cant_plati}")
    print(f"Entradas Gold:\t\t ${gold}\t Cantidad: {cant_gold}")
    print(f"Entradas Silver:\t ${silver}\t Cantidad: {cant_silver}")
    print(f"--------- Total -----------")
    print(f"Total recaudado:\t ${(plati + gold + silver)}")