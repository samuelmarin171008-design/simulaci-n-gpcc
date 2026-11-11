def solicitar_datos(): # Solicita el nombre de la planta y el nombre del supervisor
    print(" Simulador de gestion y produccion gcpp ")
    nombre_planta = str(input(" Ingrese el nombre de la planta: "))
    nombre_supervisor = str(input(" Ingrese el nombre del supervisor: "))
    return nombre_planta, nombre_supervisor

def elegir_escenario(): # Elige entre 3 escenarios
    print("\n Seleccione el escenario de produccion ")
    print("1. Escenario 1 - Produccion estable ")
    print("2. Escenario 2 - Alta demanda ")
    print("3. Escenario 3 - Produccion critica ")
    
    op = int(input(" Escriba el numero correspondiente para el escenario: (1-2-3) ")) 
    while op < 1 or op > 3: # Evita que se seleccione una opcion fuera del rango definido
        try:
            op = int(input(" Elija 1, 2 o 3: "))
            if op < 1 or op > 3:
                print(" Opcion no valida, intente de nuevo ")
        except ValueError:
            print(" Error, debe ingresar un numero entero ")
            
    return op

def cargar_variables(op): # Segun el escenario asigna variables y permite seleccionar la cantidad de materia prima de acuerdo al escenario
    if op == 1:
        horas_disponibles = 8
        estado_maquinaria = 100
        capacidad_planta = 85 
        print(" Escenario 1 Seleccionado: Mostrando recursos..")
        print(f" Horas Disponibles: {horas_disponibles}")
        print(f" Estado de la Maquinaria: {estado_maquinaria}% ")
        print(f" Capacidad de la Planta: {capacidad_planta} unidades ")
        materia_prima = int(input(" Cantidad de materia prima para usar en esta jornada: (1 - 1000) "))
        while materia_prima < 1 or materia_prima > 1000:
            try:
                materia_prima = int(input(" Ingrese una cantidad valida: (1 - 1000 ) "))
                if materia_prima < 1 or materia_prima > 1000:
                    print(" Opcion no valida, intente nuevamente ")
            except ValueError:
                print(" Error, ingrese un numero entero: ")

    elif op == 2:
        horas_disponibles = 7
        estado_maquinaria = 100
        capacidad_planta = 102  
        print(" Escenario 2 Seleccionado: Mostrando recursos..")
        print(f" Horas Disponibles: {horas_disponibles}")
        print(f" Estado de la Maquinaria: {estado_maquinaria}% ")
        print(f" Capacidad de la Planta: {capacidad_planta} unidades ")
        materia_prima = int(input(" Cantidad de materia prima para usar en esta jornada: (1000 - 1200) "))
        while materia_prima < 1000 or materia_prima > 1200:
            try:
                materia_prima = int(input(" Ingrese una cantidad valida: (1000 - 1200 ) "))
                if materia_prima < 1000 or materia_prima > 1200:
                    print(" Opcion no valida, intente nuevamente ")
            except ValueError:
                print(" Error, ingrese un numero entero: ")
        
    elif op == 3:
        horas_disponibles = 6
        estado_maquinaria = 80
        capacidad_planta = 51
        print(" Escenario 2 Seleccionado: Mostrando recursos..")
        print(f" Horas Disponibles: {horas_disponibles}")
        print(f" Estado de la Maquinaria: {estado_maquinaria}% ")
        print(f" Capacidad de la Planta: {capacidad_planta} unidades ")
        materia_prima = int(input(" Cantidad de materia prima para usar en esta jornada: (1 - 600) "))
        while materia_prima < 1 or materia_prima > 600:
            try:
                materia_prima = int(input(" Ingrese una cantidad valida: (1 - 600 ) "))
                if materia_prima < 1 or materia_prima > 600:
                    print(" Opcion no valida, intente nuevamente ")
            except ValueError:
                print(" Error, ingrese un numero entero: ")  
        
    return materia_prima, horas_disponibles, estado_maquinaria, capacidad_planta

def planificacion_calculo(): # Funcion para el calculo de la viabilidad del plan
    opcion = elegir_escenario()  # importamos variables del modulo config
    materia_prima, horas_disponibles, estado_maquinaria, capacidad_planta = cargar_variables(opcion)

    materia_prima_disponible = 5000 - materia_prima
    horas_produccion = 40 - horas_disponibles
    unidades_producir = int((materia_prima / 10) * 0.85)
    horas_por_unidad = round(horas_disponibles / unidades_producir, 2)
    estado_maquinaria_necesario = capacidad_planta - unidades_producir

    if materia_prima_disponible < 0:
        print(" No hay suficiente materia prima disponible, regresando al escenario de produccion..")

    elif horas_produccion < horas_por_unidad * unidades_producir:
        print(" Las horas de produccion totales no alcanzan para este plan ")
        
    elif estado_maquinaria_necesario > estado_maquinaria:
        print(" El estado actual de la maquinaria no permite continuar con este plan ")

    elif capacidad_planta < unidades_producir:
        print(" Las unidades a producir superan la capacidad de la planta ")

    else:
        print(" PLANIFICACION APROBADA: El plan de produccion es viable ")
        print(f" Materia prima restante: {materia_prima_disponible} ")
        print(f" Materia prima utilizada: {materia_prima} ")
        print(f" Horas restantes: {horas_produccion} ")
        print(f" Horas utilizadas: {horas_disponibles} ")
        print(f" Unidades a producir: {unidades_producir} ")
        print(f" Horas utilizadas por unidad: {horas_por_unidad} ")

        return materia_prima_disponible, horas_produccion, unidades_producir, horas_por_unidad, estado_maquinaria_necesario

planta, supervisor = solicitar_datos()
planificacion_calculo()