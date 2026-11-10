"""Modulo PROVISIONAL: produccion de una jornada con reglas simples.

Existe solo para que el simulador se pueda ejecutar de principio a fin mientras
los modulos definitivos del equipo (planificacion, produccion, incidencias,
mantenimiento, control de calidad y costos) terminan de integrarse.
Cuando esten listos, simulacion.py debe llamar a esos modulos y este archivo
se elimina.

Cada funcion devuelve UN solo valor (no se usan tuplas).

Reglas provisionales:
- Cada unidad producida consume MATERIA_POR_UNIDAD de materia prima mas un
  porcentaje de desperdicio.
- La produccion posible depende de la capacidad de la planta, el estado de la
  maquinaria, las horas realmente utilizadas y la materia prima disponible.
- Cada jornada la maquinaria se desgasta DESGASTE_POR_JORNADA puntos.
"""

MATERIA_POR_UNIDAD = 1.5
TASA_DESPERDICIO = 0.04
DESGASTE_POR_JORNADA = 6.0
COSTO_MATERIA = 2.0
COSTO_HORA_PERDIDA = 40.0
PENALIZACION_DEFECTUOSO = 5.0


def materia_disponible(escenario, jornada):
    """Materia prima que llega para la jornada (se repone en cada jornada).

    En el escenario 3 el abastecimiento cae a la mitad desde la jornada 3.
    """
    if escenario == 1:
        materia = 1000.0
    elif escenario == 2:
        materia = 1200.0
    else:
        materia = 600.0
    if escenario == 3 and jornada >= 3:
        materia = materia * 0.5
    return materia


def horas_disponibles(escenario):
    """Horas de operacion de la jornada segun el escenario."""
    if escenario == 1:
        return 8.0
    elif escenario == 2:
        return 7.0
    return 6.0


def capacidad_planta(escenario):
    """Capacidad maxima de produccion de la jornada segun el escenario."""
    if escenario == 1:
        return 600.0
    elif escenario == 2:
        return 700.0
    return 300.0


def estado_maquinaria_inicial(escenario):
    """Estado inicial de la maquinaria (0 a 100) segun el escenario."""
    if escenario == 3:
        return 80.0
    return 100.0


def calcular_produccion_planificada(escenario, capacidad):
    """Plan de la jornada: un porcentaje de la capacidad segun el escenario."""
    if escenario == 1:
        return int(capacidad * 0.80)
    elif escenario == 2:
        return int(capacidad * 0.95)
    return int(capacidad * 0.90)


def calcular_horas_perdidas(escenario, jornada):
    """Horas perdidas por incidencias: ocurren en las jornadas pares."""
    if jornada % 2 == 0:
        return 1.0 + (escenario - 1) * 0.5
    return 0.0


def calcular_produccion_realizada(produccion_planificada, capacidad, estado_maquinaria,
                                  horas_utilizadas, horas_disponibles_jornada,
                                  materia_prima):
    """Produccion obtenida: lo menor entre el plan y lo que permiten los recursos."""
    por_capacidad = capacidad * (estado_maquinaria / 100) * (horas_utilizadas / horas_disponibles_jornada)
    por_materia = materia_prima / (MATERIA_POR_UNIDAD * (1 + TASA_DESPERDICIO))
    realizada = produccion_planificada
    if por_capacidad < realizada:
        realizada = por_capacidad
    if por_materia < realizada:
        realizada = por_materia
    return int(realizada)


def calcular_desperdicio(produccion_realizada):
    """Material perdido en el proceso."""
    return produccion_realizada * MATERIA_POR_UNIDAD * TASA_DESPERDICIO


def calcular_materia_consumida(produccion_realizada):
    """Materia prima consumida (incluye el desperdicio)."""
    return produccion_realizada * MATERIA_POR_UNIDAD + calcular_desperdicio(produccion_realizada)


def calcular_defectuosos(produccion_realizada, estado_maquinaria):
    """Unidades defectuosas: la tasa sube cuando la maquinaria esta mas desgastada."""
    tasa = 0.02 + ((100 - estado_maquinaria) / 100) * 0.25
    return int(produccion_realizada * tasa)


def calcular_eficiencia(horas_utilizadas, horas_disponibles_jornada, estado_maquinaria):
    """Eficiencia = uso del tiempo * estado de la maquinaria (en porcentaje)."""
    return (horas_utilizadas / horas_disponibles_jornada) * (estado_maquinaria / 100) * 100


def calcular_costo_jornada(materia_consumida, horas_perdidas, defectuosos):
    """Costo = materia prima + tiempo perdido + penalizacion por defectuosos."""
    return (materia_consumida * COSTO_MATERIA
            + horas_perdidas * COSTO_HORA_PERDIDA
            + defectuosos * PENALIZACION_DEFECTUOSO)


def aplicar_desgaste(estado_maquinaria):
    """Estado de la maquinaria para la siguiente jornada (nunca menor a 0)."""
    nuevo_estado = estado_maquinaria - DESGASTE_POR_JORNADA
    if nuevo_estado < 0:
        return 0.0
    return nuevo_estado
