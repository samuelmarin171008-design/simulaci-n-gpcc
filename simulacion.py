"""Modulo del ciclo de jornadas y del reinicio.

Coordina las 5 jornadas de una simulacion: en cada una calcula la produccion,
evalua el estado de la jornada, acumula los totales y al final muestra el
informe final.
Tambien pregunta si se desea reiniciar la simulacion.

PUNTO DE INTEGRACION: las llamadas a `jornada_provisional` (alias `jornada`)
son las que se deben reemplazar por los modulos definitivos del equipo
(planificacion, produccion, incidencias/decisiones, mantenimiento, control de
calidad y costos).
"""

import evaluacion
import jornada_provisional as jornada
import utilidades

TOTAL_JORNADAS = 5
# Porcentaje de la materia disponible que debe sobrar para considerar que los
# recursos son suficientes de cara a la siguiente jornada.
MATERIA_MINIMA_PORCENTAJE = 10.0


def ejecutar_simulacion(escenario):
    """Ejecuta las 5 jornadas del escenario elegido y muestra el informe final."""
    # Acumulados de toda la simulacion
    total_planificado = 0
    total_realizado = 0
    total_defectuosos = 0
    desperdicio_acumulado = 0.0
    materia_consumida_total = 0.0
    horas_utilizadas_total = 0.0
    horas_perdidas_total = 0.0
    suma_eficiencias = 0.0
    costo_acumulado = 0.0
    jornadas_superadas = 0
    jornadas_sin_recursos = 0
    estado_maquinaria = jornada.estado_maquinaria_inicial(escenario)

    jornada_actual = 1
    while jornada_actual <= TOTAL_JORNADAS:
        print(f"\n===== JORNADA {jornada_actual} DE {TOTAL_JORNADAS} =====")

        # 1. Planificacion
        materia_prima = jornada.materia_disponible(escenario, jornada_actual)
        horas_disp = jornada.horas_disponibles(escenario)
        capacidad = jornada.capacidad_planta(escenario)
        produccion_planificada = jornada.calcular_produccion_planificada(escenario, capacidad)

        # 2-3. Produccion e incidencia (horas perdidas)
        horas_perdidas = jornada.calcular_horas_perdidas(escenario, jornada_actual)
        horas_utilizadas = horas_disp - horas_perdidas
        produccion_realizada = jornada.calcular_produccion_realizada(
            produccion_planificada, capacidad, estado_maquinaria,
            horas_utilizadas, horas_disp, materia_prima)

        # 4-5. Actualizacion de variables de la jornada
        desperdicio = jornada.calcular_desperdicio(produccion_realizada)
        materia_consumida = jornada.calcular_materia_consumida(produccion_realizada)
        defectuosos = jornada.calcular_defectuosos(produccion_realizada, estado_maquinaria)
        costo = jornada.calcular_costo_jornada(materia_consumida, horas_perdidas, defectuosos)
        materia_restante = materia_prima - materia_consumida

        # 6. Control: indicadores de la jornada
        cumplimiento = utilidades.calcular_porcentaje(produccion_realizada, produccion_planificada)
        calidad = evaluacion.calcular_calidad(produccion_realizada, defectuosos)
        porcentaje_desperdicio = utilidades.calcular_porcentaje(desperdicio, materia_consumida)
        eficiencia = jornada.calcular_eficiencia(horas_utilizadas, horas_disp, estado_maquinaria)
        materia_minima = materia_prima * (MATERIA_MINIMA_PORCENTAJE / 100)

        # 7. Reporte: evaluacion de la jornada
        print(f"Planificado: {produccion_planificada} | Realizado: {produccion_realizada} "
              f"| Defectuosos: {defectuosos} | Maquinaria: {estado_maquinaria:.0f}%")
        estado_jornada = evaluacion.mostrar_evaluacion_jornada(
            jornada_actual, cumplimiento, calidad, porcentaje_desperdicio,
            eficiencia, materia_restante, materia_minima)

        # Acumulacion de totales
        total_planificado = total_planificado + produccion_planificada
        total_realizado = total_realizado + produccion_realizada
        total_defectuosos = total_defectuosos + defectuosos
        desperdicio_acumulado = desperdicio_acumulado + desperdicio
        materia_consumida_total = materia_consumida_total + materia_consumida
        horas_utilizadas_total = horas_utilizadas_total + horas_utilizadas
        horas_perdidas_total = horas_perdidas_total + horas_perdidas
        suma_eficiencias = suma_eficiencias + eficiencia
        costo_acumulado = costo_acumulado + costo
        if estado_jornada == "JORNADA SUPERADA":
            jornadas_superadas = jornadas_superadas + 1
        if evaluacion.clasificar_recursos(materia_restante, materia_minima) == "Insuficientes":
            jornadas_sin_recursos = jornadas_sin_recursos + 1

        # Paso a la siguiente jornada
        estado_maquinaria = jornada.aplicar_desgaste(estado_maquinaria)
        if jornada_actual < TOTAL_JORNADAS:
            utilidades.pausar("\nPresione Enter para continuar a la siguiente jornada...")
        jornada_actual = jornada_actual + 1

    return evaluacion.mostrar_informe_final(
        total_planificado, total_realizado, total_defectuosos,
        desperdicio_acumulado, materia_consumida_total,
        horas_utilizadas_total, horas_perdidas_total, suma_eficiencias,
        costo_acumulado, jornadas_superadas, jornadas_sin_recursos, TOTAL_JORNADAS)


def preguntar_nueva_simulacion():
    """Muestra el menu Si/No y devuelve True si el usuario quiere reiniciar."""
    print("\nDesea ejecutar una nueva simulacion?\n")
    print("1. Si")
    print("2. No\n")
    opcion = utilidades.leer_entero_en_rango("Seleccione una opcion: ", 1, 2)
    return opcion == 1
