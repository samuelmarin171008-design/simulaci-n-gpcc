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
    
    return unidades_producir, materia_prima_disponible, horas_produccion, demanda_establecida, capacidad_planta, materia_prima, estado_maquinaria

def planificacion_verificacion(): # Sistema para verificar si el plan es viable
    unidades_producir, materia_prima_disponible, horas_produccion, demanda_establecida, capacidad_planta, materia_prima, estado_maquinaria = planificacion_calculo()

    if demanda_establecida > capacidad_planta:
        print(" Error: La demanda establecida es mayor que la capacidad de la planta ")
        respuesta = str(input(" ¿Desea cambiar de plan de produccion? (Si/No) ")).lower()

        if respuesta == "si":
            return config.elegir_escenario() # Volvera a seleccionar el escenario de produccion

        elif respuesta == "no":
            print(" Recortando materia prima a la mitad para esta jornada para no sobrepasar la capacidad de la planta.. ")
            materia_prima = materia_prima / 2
            planificacion_calculo() # Hara los calculos nuevamente con la variable actualizada




        





# Verificar si es viable
# Si algo no es viable debera: advertir la situacion, impedir o modificar el plan
# o afectar una variable
