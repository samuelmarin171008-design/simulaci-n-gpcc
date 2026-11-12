import config
materia_prima_disponible, horas_produccion, unidades_producir, horas_por_unidad, estado_maquinaria_necesario, materia_prima, horas_disponibles, capacidad_planta, estado_maquinaria = config.planificacion_calculo
def calcular_costos(materia_prima):
    costo_materia = materia_prima * 2
    costo_extra = 50
    costo_total = costo_materia + costo_extra
    return costo_total

def calcular_indicadores(unidades_producir, demanda, horas_disponibles, horas_gastadas):
    if unidades_producir > 0:
        cumplimiento = (demanda / unidades_producir) * 100
    else:
        cumplimiento = 0.0
        
    if horas_disponibles > 0:
        eficiencia = (horas_gastadas / horas_disponibles) * 100
    else:
        eficiencia = 0.0
        
    return cumplimiento, eficiencia

def principal():
    materia_usada =+ materia_prima
    costo_total = calcular_costos(materia_usada)
    cumplimiento, eficiencia = calcular_indicadores(unidades_producir, demanda_est, horas_disponibles, horas_gastadas)
    
    print("PANEL DE ESTADO Y REPORTES")
    print("Unidades a producir      :", unidades_producir)
    print("Materia prima disponible :", materia_prima_disponible)
    print("Horas gastadas           :", horas_gastadas)
    print("Demanda establecida      :", demanda_est)
    print("Cumplimiento             :", round(cumplimiento, 1), "%")
    print("Eficiencia               :", round(eficiencia, 1), "%")
    print("Costo total de jornada   : $", costo_total)
    
    if demanda_est >= (unidades_producir * 0.9):
        print("RESULTADO: PLAN DE PRODUCCION CUMPLIDO")
    else:
        print("RESULTADO: PLAN DE PRODUCCION INCUMPLIDO")

principal()
