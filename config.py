def solicitar_datos():
    print("simulador de gestion y produccion gcpp")
    nombre_planta = input("ingrese el nombre de la planta: ")
    nombre_supervisor = input("ingrese el nombre del supervisor: ")
    return nombre_planta, nombre_supervisor

def elegir_escenario():
    print("\nseleccione el escenario de produccion")
    print("1. escenario 1 - produccion estable")
    print("2. escenario 2 - alta demanda")
    print("3. escenario 3 - produccion critica")
    
    op = 0
    while op < 1 or op > 3:
        try:
            op = int(input("elija 1, 2 o 3: "))
            if op < 1 or op > 3:
                print("opcion no valida, intente de nuevo")
        except ValueError:
            print("error, debe ingresar un numero entero")
            
    return op

def cargar_variables(opcion_escenario):
    if opcion_escenario == 1:
        materia_prima = 1000
        horas_disponibles = 40
        estado_maquinaria = 100
    elif opcion_escenario == 2:
        materia_prima = 1200
        horas_disponibles = 40
        estado_maquinaria = 100
    else:
        materia_prima = 600
        horas_disponibles = 30
        estado_maquinaria = 80
        
    return materia_prima, horas_disponibles, estado_maquinaria

def panel_estado(jornada, materia_prima, horas_disp, estado_maq):
    print("\n----------------------------------------")
    print("      panel de estado - jornada " + str(jornada))
    print("----------------------------------------")
    print("materia prima disponible: " + str(materia_prima))
    print("horas de trabajo disponibles: " + str(horas_disp))
    print("estado de la maquinaria: " + str(estado_maq) + "%")
    print("----------------------------------------")