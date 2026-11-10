"""Modulo de evaluacion: de cada jornada y de la simulacion completa.

Parte 1 - Evaluacion de la jornada: analiza produccion, calidad, desperdicio,
eficiencia y recursos, y determina el estado de la jornada (superada, en riesgo...).
Parte 2 ( en fase de construccion ) - Resultado final: calcula los indicadores globales de las 5 jornadas,
determina cual de los 5 resultados finales se obtuvo y muestra el informe final.
"""

from utilidades import calcular_porcentaje, no_negativo

# --- Rangos de evaluacion (en porcentaje) ---
CUMPLIMIENTO_CUMPLIDA = 90.0   # si >= 90  -> Cumplida
CUMPLIMIENTO_EN_RIESGO = 70.0  # de 70-89  -> En riesgo ; < 70 -> No cumplida
CALIDAD_ACEPTABLE = 95.0       # si >= 95  -> Aceptable
CALIDAD_ATENCION = 90.0        # de 90-94  -> En atencion ; si < 90 -> Critica
DESPERDICIO_CONTROLADO = 5.0   # si <= 5   -> Controlado
DESPERDICIO_ELEVADO = 10.0     # entre 5-10   -> Elevado ; si > 10 -> Excesivo
EFICIENCIA_ALTA = 85.0         # si >= 85  -> Alta
EFICIENCIA_MEDIA = 70.0        # entre 70-84  -> Media ; si < 70 -> Baja


def clasificar_produccion(cumplimiento):
    """Clasifica el cumplimiento de produccion de la jornada."""
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

#valores de resultados aun en construccion
