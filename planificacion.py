import config

def planificacion_calculo(): # Funcion para el calculo de la viabilidad de plan
    opcion = config.elegir_escenario()  # importamos variables del modulo config
    materia_prima, horas_disponibles, estado_maquinaria, capacidad_planta = config.cargar_variables(opcion)

   
    unidades_producir = int((materia_prima / 2) * 0.85)
    materia_prima_disponible = 5000 - materia_prima
    horas_produccion = 40 - horas_disponibles
    demanda_establecida = int((unidades_producir * (estado_maquinaria / 100)))
    
    return unidades_producir, materia_prima_disponible, horas_produccion, demanda_establecida, capacidad_planta, materia_prima, estado_maquinaria

def planificacion_verificacion(): # Verificacion de la viabilidad de plan
    unidades_producir, materia_prima_disponible, horas_produccion, demanda_establecida, capacidad_planta, materia_prima, estado_maquinaria = planificacion_calculo()

    if demanda_establecida > capacidad_planta:
        print(" ERROR: La demanda establecida es mayor que la capacidad de la planta ")
        print(" Devolviendo a Seleccion de Plan de Produccion..")
        return config.elegir_escenario() 

    elif materia_prima_disponible < materia_prima:
        print(" ERROR: No hay suficiente materia prima disponible para la produccion completa. ")
        print(" Ajustando recursos.. ")
        materia_prima = materia_prima_disponible
    else:
        print("--- PLANIFICACION EXITOSA ---")
        print(f" Unidades a producir: {unidades_producir}")
        print(f" Demanda establecida: {demanda_establecida}")
        print(f" Materia prima restante: {materia_prima_disponible}")


planta, supervisor = config.solicitar_datos()
planificacion_verificacion()