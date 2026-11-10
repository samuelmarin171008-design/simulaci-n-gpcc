"""Modulo de evaluacion: de cada jornada y de la simulacion completa.

Parte 1 - Evaluacion de la jornada: analiza produccion, calidad, desperdicio,
eficiencia y recursos, y determina el estado de la jornada (superada, en riesgo...).
Parte 2 - Resultado final: calcula los indicadores globales de las 5 jornadas,
determina cual de los 5 resultados finales se obtuvo y muestra el informe final.
"""

from utilidades import calcular_porcentaje, no_negativo

# --- Umbrales de evaluacion (en porcentaje) ---
CUMPLIMIENTO_CUMPLIDA = 90.0   # >= 90  -> Cumplida
CUMPLIMIENTO_EN_RIESGO = 70.0  # 70-89  -> En riesgo ; < 70 -> No cumplida
CALIDAD_ACEPTABLE = 95.0       # >= 95  -> Aceptable
CALIDAD_ATENCION = 90.0        # 90-94  -> En atencion ; < 90 -> Critica
DESPERDICIO_CONTROLADO = 5.0   # <= 5   -> Controlado
DESPERDICIO_ELEVADO = 10.0     # 5-10   -> Elevado ; > 10 -> Excesivo
EFICIENCIA_ALTA = 85.0         # >= 85  -> Alta
EFICIENCIA_MEDIA = 70.0        # 70-84  -> Media ; < 70 -> Baja


def clasificar_produccion(cumplimiento):
    """Clasifica el cumplimiento de produccion (%) de la jornada."""
    if cumplimiento >= CUMPLIMIENTO_CUMPLIDA:
        return "Cumplida"
    elif cumplimiento >= CUMPLIMIENTO_EN_RIESGO:
        return "En riesgo"
    else:
        return "No cumplida"


def clasificar_calidad(calidad):
    """Clasifica el porcentaje de calidad de la jornada."""
    if calidad >= CALIDAD_ACEPTABLE:
        return "Aceptable"
    elif calidad >= CALIDAD_ATENCION:
        return "En atencion"
    else:
        return "Critica"


def clasificar_desperdicio(porcentaje_desperdicio):
    """Clasifica el porcentaje de material desperdiciado."""
    if porcentaje_desperdicio <= DESPERDICIO_CONTROLADO:
        return "Controlado"
    elif porcentaje_desperdicio <= DESPERDICIO_ELEVADO:
        return "Elevado"
    else:
        return "Excesivo"


def clasificar_eficiencia(eficiencia):
    """Clasifica el porcentaje de eficiencia de la jornada."""
    if eficiencia >= EFICIENCIA_ALTA:
        return "Alta"
    elif eficiencia >= EFICIENCIA_MEDIA:
        return "Media"
    else:
        return "Baja"


def clasificar_recursos(materia_restante, materia_minima):
    """Indica si la materia prima restante alcanza para continuar.

    'Insuficientes' cuando lo que queda es menor que el minimo necesario.
    """
    if materia_restante >= materia_minima:
        return "Suficientes"
    return "Insuficientes"


def determinar_estado_jornada(produccion, calidad, desperdicio, eficiencia, recursos):
    """Combina los estados individuales en el estado final de la jornada.

    El orden de las condiciones indica la prioridad: primero los problemas mas
    graves (calidad, recursos) y por ultimo el cumplimiento de la produccion.
    """
    if calidad == "Critica":
        return "CALIDAD CRITICA"
    elif recursos == "Insuficientes":
        return "RECURSOS INSUFICIENTES"
    elif produccion == "No cumplida":
        return "JORNADA NO CUMPLIDA"
    elif produccion == "En riesgo":
        return "PRODUCCION EN RIESGO"
    elif calidad == "Aceptable" and desperdicio != "Excesivo" and eficiencia != "Baja":
        return "JORNADA SUPERADA"
    else:
        return "JORNADA SUPERADA CON OBSERVACIONES"


def mostrar_evaluacion_jornada(numero_jornada, cumplimiento, calidad,
                               porcentaje_desperdicio, eficiencia,
                               materia_restante, materia_minima):
    """Evalua la jornada, muestra el resultado en pantalla y devuelve su estado."""
    produccion = clasificar_produccion(cumplimiento)
    estado_calidad = clasificar_calidad(calidad)
    desperdicio = clasificar_desperdicio(porcentaje_desperdicio)
    estado_eficiencia = clasificar_eficiencia(eficiencia)
    recursos = clasificar_recursos(materia_restante, materia_minima)
    estado_jornada = determinar_estado_jornada(
        produccion, estado_calidad, desperdicio, estado_eficiencia, recursos)

    print("-" * 60)
    print(f"ESTADO DE LA JORNADA {numero_jornada}")
    print(f"Produccion : {produccion} ({cumplimiento:.1f}%)")
    print(f"Calidad    : {estado_calidad} ({calidad:.1f}%)")
    print(f"Desperdicio: {desperdicio} ({porcentaje_desperdicio:.1f}%)")
    print(f"Eficiencia : {estado_eficiencia} ({eficiencia:.1f}%)")
    print(f"Recursos   : {recursos}")
    print("-" * 36)
    print(estado_jornada)
    print("-" * 60)
    return estado_jornada


# ====================== RESULTADO FINAL ======================
# --- Condiciones de los resultados finales (en porcentaje) ---
CUMPLIMIENTO_SATISFACTORIO = 90.0  # >= 90 (y calidad >= 90) -> satisfactorio
CUMPLIMIENTO_PARCIAL = 70.0        # 70-89                   -> parcial
CALIDAD_SATISFACTORIA = 90.0       # calidad minima para el resultado satisfactorio
CALIDAD_CRITICA = 85.0             # calidad final < 85      -> critico por calidad
JORNADAS_SIN_RECURSOS_CRITICAS = 40.0  # % de jornadas con recursos insuficientes
HORAS_PERDIDAS_CRITICAS = 30.0     # % de horas perdidas sobre las disponibles


def calcular_calidad(unidades_producidas, unidades_defectuosas):
    """Porcentaje de calidad = unidades aceptadas / unidades producidas * 100.

    Si no se produjo nada, no hay defectos: devuelve 100.0 (el problema de esa
    situacion lo captura el cumplimiento, no la calidad).
    """
    if unidades_producidas > 0:
        aceptadas = unidades_producidas - unidades_defectuosas
        return calcular_porcentaje(aceptadas, unidades_producidas)
    return 100.0


def calcular_eficiencia_final(suma_eficiencias, total_jornadas):
    """Eficiencia final = promedio de las eficiencias de todas las jornadas."""
    if total_jornadas > 0:
        return suma_eficiencias / total_jornadas
    return 0.0


def hay_recursos_agotados(jornadas_sin_recursos, total_jornadas,
                          horas_utilizadas, horas_perdidas):
    """True si faltaron recursos de forma grave durante la simulacion.

    Ocurre cuando hubo muchas jornadas con materia insuficiente o se perdio una
    parte importante de las horas disponibles.
    """
    porcentaje_jornadas = calcular_porcentaje(jornadas_sin_recursos, total_jornadas)
    porcentaje_horas = calcular_porcentaje(horas_perdidas, horas_utilizadas + horas_perdidas)
    return (porcentaje_jornadas >= JORNADAS_SIN_RECURSOS_CRITICAS
            or porcentaje_horas >= HORAS_PERDIDAS_CRITICAS)


def determinar_resultado_final(cumplimiento, calidad_final, recursos_agotados):
    """Devuelve el resultado general de la planta (uno de 5 posibles).

    El orden indica la prioridad: primero las situaciones criticas.
    """
    if calidad_final < CALIDAD_CRITICA:
        return "RESULTADO CRITICO POR PROBLEMAS DE CALIDAD"
    elif cumplimiento < CUMPLIMIENTO_SATISFACTORIO and recursos_agotados:
        return "RESULTADO CRITICO POR FALTA DE RECURSOS"
    elif cumplimiento >= CUMPLIMIENTO_SATISFACTORIO and calidad_final >= CALIDAD_SATISFACTORIA:
        return "PLAN DE PRODUCCION CUMPLIDO"
    elif cumplimiento >= CUMPLIMIENTO_PARCIAL:
        return "PLAN DE PRODUCCION CUMPLIDO PARCIALMENTE"
    else:
        return "PLAN DE PRODUCCION INCUMPLIDO"


def mostrar_informe_final(total_planificado, total_realizado, total_defectuosos,
                          desperdicio_acumulado, materia_consumida_total,
                          horas_utilizadas, horas_perdidas, suma_eficiencias,
                          costo_acumulado, jornadas_superadas, jornadas_sin_recursos,
                          total_jornadas):
    """Calcula los indicadores globales, muestra el informe y devuelve el resultado."""
    pendiente = no_negativo(total_planificado - total_realizado)
    cumplimiento = calcular_porcentaje(total_realizado, total_planificado)
    calidad_final = calcular_calidad(total_realizado, total_defectuosos)
    porcentaje_desperdicio = calcular_porcentaje(desperdicio_acumulado, materia_consumida_total)
    eficiencia_final = calcular_eficiencia_final(suma_eficiencias, total_jornadas)
    recursos_agotados = hay_recursos_agotados(
        jornadas_sin_recursos, total_jornadas, horas_utilizadas, horas_perdidas)
    resultado = determinar_resultado_final(cumplimiento, calidad_final, recursos_agotados)

    print("\n" + "=" * 40)
    print("            INFORME FINAL")
    print("=" * 40)
    print()
    print(f"Produccion planificada : {total_planificado}")
    print(f"Produccion realizada   : {total_realizado}")
    print(f"Produccion pendiente   : {pendiente}")
    print(f"Cumplimiento           : {cumplimiento:.1f}%")
    print()
    print(f"Productos defectuosos  : {total_defectuosos}")
    print(f"Calidad final          : {calidad_final:.1f}%")
    print(f"Desperdicio acumulado  : {desperdicio_acumulado:.1f} ({porcentaje_desperdicio:.1f}%)")
    print()
    print(f"Horas utilizadas       : {horas_utilizadas:.1f}")
    print(f"Horas perdidas         : {horas_perdidas:.1f}")
    print(f"Eficiencia final       : {eficiencia_final:.1f}%")
    print()
    print(f"Costo acumulado        : ${costo_acumulado:.2f}")
    print(f"Jornadas superadas     : {jornadas_superadas} de {total_jornadas}")
    print()
    print("RESULTADO:")
    print(resultado)
    print("=" * 40)
    return resultado
