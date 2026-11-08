# Variables de la simulacion
import config

def variables_simulacion(): # Definimos las variables que utilizaremos
    opcion = config.elegir_escenario() # Importamos variables del modulo config.py
    materia_prima, horas_disponibles, estado_maquinaria = config.cargar_variables(opcion)
    
    # Variables de tiempo
    produccion_planificada = 100
    produccion_realizada = 0
    horas_utilizadas = 0
    horas_perdidas = 0
    jornadas_restantes = 5

    # Variables de productos
    unidades_produccion = (materia_prima / jornadas_restantes) * 0.85
    productos_defectuosos = 0
    desperdicio = 0

    # De aca para abajo esta incompleto (importante)
    calidad = 0
    costo_acumulado = 0
    eficiencia = 0
    cumplimiento_produccion = 0

    # 3. Retornamos
    return (
        materia_prima,
        horas_disponibles,
        estado_maquinaria,
        produccion_planificada,
        produccion_realizada,
        productos_defectuosos,
        desperdicio,
        horas_utilizadas,
        horas_perdidas,
        calidad,
        costo_acumulado,
        eficiencia,
        cumplimiento_produccion
    )

# Planificacion de produccion
# Antes de iniciar cada jornada el sistema debe de establecer un plan de produccion

# Considerar variables como:
# Cantidad de unidades a producir
# Materia prima disponible
# Horas de produccion
# Capacidad de la planta
# Demanda establecida

# Verificar si es viable
# Si algo no es viable debera: advertir la situacion, impedir o modificar el plan
# o afectar una variable
