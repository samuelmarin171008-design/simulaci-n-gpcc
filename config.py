def inicializar_simulacion():
    """
    inicializa y retorna todas las variables escalares requeridas 
    por los diferentes módulos del diagrama de flujo de la simulación
    """
    
    # Configuración Inicial y Escenarios
    jornada_actual = 1
    escenario = 1  # 1: Estable, 2: Alta Demanda, 3: Crítica
    
    # Recursos y Producción
    materia_prima = 100.0
    horas_disponibles = 8.0
    produccion_planificada = 50.0
    produccion_realizada = 0.0
    
    # 3. Sistema de Incidencias y Decisiones (A, B, C)
    tipo_incidencia = 0      # 0: Ninguna, 1: Leve, 2: Grave
    decision_tomada = "Ninguna"
    consecuencia_aplicada = "Ninguna"
    
    # 4. Sistema de Mantenimiento y Maquinaria
    estado_maquinaria = 100.0   # Porcentaje (0 a 100)
    requiere_mantenimiento = False
    accion_mantenimiento = 0    # 1: Realizar, 2: No realizar
    
    # 5. Control de Calidad e Indicadores
    control_calidad_aprobado = True
    tasa_defectuosos = 0.0
    
    # 6. Sistema de Costos y Evaluación
    costos_operativos = 0.0
    costos_mantenimiento = 0.0
    costo_total = 0.0
    resultado_jornada = "Pendiente"
    
    # Retornamos todas las variables de forma escalar en orden
    return (
        jornada_actual,
        escenario,
        materia_prima,
        horas_disponibles,
        produccion_planificada,
        produccion_realizada,
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


def panel_estado(jornada, escenario, mp, horas, plan, real, maq, calidad, costos):
    """
    Muestra el panel de estado global para llevar el control detallado 
    en cada jornada y decisión importante del proceso
    """
    print("\n" + "=" * 55)
    print(f"       PANEL DE ESTADO - JORNADA {jornada} (Escenario {escenario})")
    print("=" * 55)
    print(f" * Materia Prima Disponible : {mp}")
    print(f" * Horas Disponibles        : {horas} hrs")
    print(f" * Producción Planificada   : {plan}")
    print(f" * Producción Realizada     : {real}")
    print(f" * Estado de Maquinaria     : {maq}%")
    print(f" * Control de Calidad       : {'Aprobado' if calidad else 'Rechazado'}")
    print(f" * Costos Acumulados        : ${costos}")
    print("=" * 55 + "\n")
