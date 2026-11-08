def inicializar_simulacion():
    jornada_actual = 1
    escenario = 1
    materia_prima = 100.0
    horas_disponibles = 8.0
    demanda_estimada = 50.0
    eficiencia_planificada = 1.0
    produccion_planificada = 50.0
    produccion_realizada = 0.0
    advertencia_situacion = False
    modificar_plan = False
    tipo_incidencia = 0
    decision_tomada = "ninguna"
    consecuencia_aplicada = "ninguna"
    estado_maquinaria = 100.0
    requiere_mantenimiento = False
    accion_mantenimiento = 0
    control_calidad_aprobado = True
    tasa_defectuosos = 0.0
    costos_operativos = 0.0
    costos_mantenimiento = 0.0
    costo_total = 0.0
    resultado_jornada = "pendiente"
    return (
        jornada_actual,
        escenario,
        materia_prima,
        horas_disponibles,
        demanda_estimada,
        eficiencia_planificada,
        produccion_planificada,
        produccion_realizada,
        advertencia_situacion,
        modificar_plan,
        tipo_incidencia,
        decision_tomada,
        consecuencia_aplicada,
        estado_maquinaria,
        requiere_mantenimiento,
        accion_mantenimiento,
        control_calidad_aprobado,
        tasa_defectuosos,
        costos_operativos,
        costos_mantenimiento,
        costo_total,
        resultado_jornada
    )