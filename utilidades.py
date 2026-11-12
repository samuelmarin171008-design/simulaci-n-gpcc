"""Modulo de utilidades: funciones de apoyo usadas por varios modulos.

Contiene la validacion de entradas por teclado y calculos auxiliares
(porcentajes). No guarda informacion: todo se maneja con parametros y retornos.
"""


def calcular_porcentaje(parte, total):
    """Devuelve (parte / total) * 100.

    Si el total es 0 devuelve 0.0 para evitar la division entre cero.
    """
    if total > 0:
        return (parte / total) * 100
    return 0.0


def no_negativo(valor):
    """Devuelve el valor recibido, o 0 si el valor es negativo."""
    if valor < 0:
        return 0
    return valor


def leer_entero_en_rango(mensaje, minimo, maximo):
    """Pide un numero entero por teclado hasta que sea valido.

    Repite la pregunta mientras el usuario escriba algo que no sea un entero
    (try-except) o un numero fuera del rango [minimo, maximo].
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo and valor <= maximo:
                return valor
            print(f" Opcion no valida, escriba un numero entre {minimo} y {maximo} ")
        except ValueError:
            print(" Error, debe ingresar un numero entero ")


def pausar(mensaje):
    """Detiene el programa hasta que el usuario presione Enter."""
    input(mensaje)
