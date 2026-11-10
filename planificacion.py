# Variables para la Planificacion de Produccion
import config

def planificacion_calculo(): 
    opcion = config.elegir_escenario() # Importamos variables del modulo config.py
    materia_prima, horas_disponibles, estado_maquinaria, capacidad_planta = config.cargar_variables(opcion)

    # Formulas de acuerdo a las variables anteriores
    unidades_producir = int((materia_prima / 2) * 0.85)
    materia_prima_disponible = 5000 - materia_prima
    horas_produccion = 40 - horas_disponibles
    demanda_establecida = int((unidades_producir * (estado_maquinaria / 100)))
    
    return unidades_producir, materia_prima_disponible, horas_produccion, horas_disponibles, demanda_establecida, capacidad_planta, materia_prima, estado_maquinaria

def planificacion_verificacion(): # Sistema para verificar si el plan es viable
    unidades_producir, materia_prima_disponible, horas_produccion, horas_disponibles, demanda_establecida, capacidad_planta, materia_prima, estado_maquinaria = planificacion_calculo()
    if demanda_establecida > capacidad_planta:
        print(" ERROR: La demanda establecida es mayor que la capacidad de la planta ")
        print(" Devolviendo a Seleccion de Plan de Produccion..")
        return config.elegir_escenario() # Volvera a seleccionar el escenario de produccion

    elif materia_prima_disponible < materia_prima:
        print(" ERROR: No hay suficiente materia prima disponible para la produccion completa. ")
        print(" Ajustando recursos.. ")
        materia_prima = materia_prima_disponible 
        return materia_prima

    elif horas_produccion < horas_disponibles:
        print(" ERROR: No hay suficientes horas de produccion")
        print(" Seleccione un plan de produccion mas ajustado ")
        return config.elegir_escenario()

    else:
        print( " ¡El Plan de Produccion es Viable! ")

    
