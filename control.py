
def calcular_costos_jornada(materia_usada, costo_extra_incidencia):
    costo_materia = materia_usada * 2
    costo_total_jornada = costo_materia + costo_extra_incidencia
    return costo_total_jornada

def calcular_indicadores(prod_planificada, prod_real, horas_disp, horas_usadas):
    if prod_planificada > 0:
        cumplimiento = (prod_real / prod_planificada) * 100
    else:
        cumplimiento = 0.0
        
    if horas_disp > 0:
        eficiencia = (horas_usadas / horas_disp) * 100
    else:
        eficiencia = 0.0
        
    return cumplimiento, eficiencia

def mostrar_panel_estado(prod_plan, prod_real, mat_disp, horas_disp, horas_usadas, defectos, calidad, costo, cumplimiento, eficiencia):
    print(f"Produccion planificada : {prod_plan}")
    print(f"Produccion realizada   : {prod_real}")
    print(f"Materia prima restante : {mat_disp}")
    print(f"Horas usadas / disp.   : {horas_usadas} / {horas_disp}")
    print(f"Productos defectuosos  : {defectos}")
    print(f"Calidad del producto   : {calidad:.1f}%")
    print(f"Cumplimiento           : {cumplimiento:.1f}%")
    print(f"Eficiencia             : {eficiencia:.1f}%")
    print(f"Costo acumulado        : ${costo}")   

def mostrar_informe_final(total_plan, total_real, total_defectos, calidad_final, eficiencia_final, costo_final):
    print(f"Total planificado  : {total_plan}")
    print(f"Total realizado    : {total_real}")
    print(f"Calidad final      : {calidad_final:.1f}%")
    print(f"Eficiencia final   : {eficiencia_final:.1f}%")
    print(f"Costo acumulado    : ${costo_final}")
    
    if total_real >= (total_plan * 0.9):
        print("RESULTADO: PLAN DE PRODUCCION CUMPLIDO")
    else:
        print("RESULTADO: PLAN DE PRODUCCION INCUMPLIDO")
    