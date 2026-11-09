<<<<<<< HEAD
# Módulo config.py

def solicitar_datos(): 
    print(" Simulador de gestion y produccion gcpp ")
    nombre_planta = str(input(" Ingrese el nombre de la planta: "))
    nombre_supervisor = str(input(" Ingrese el nombre del supervisor: "))
    return nombre_planta, nombre_supervisor

def elegir_escenario(): 
    print("\n Seleccione el escenario de produccion ")
    print("1. Escenario 1 - Produccion estable ")
    print("2. Escenario 2 - Alta demanda ")
    print("3. Escenario 3 - Produccion critica ")
    
    op = int(input(" Escriba el numero correspondiente para el escenario: "))
    while op < 1 or op > 3: 
        try:
            op = int(input(" Elija 1, 2 o 3: "))
            if op < 1 or op > 3:
                print(" Opcion no valida, intente de nuevo ")
        except ValueError:
            print(" Error, debe ingresar un numero entero ")
            
    return op

def cargar_variables(op): 
    if op == 1:
        materia_prima = 1000
        horas_disponibles = 8
        estado_maquinaria = 100
        capacidad_planta = 600  # <--- Subido para que supere la demanda (425)
    elif op == 2:
        materia_prima = 1200
        horas_disponibles = 7
        estado_maquinaria = 100
        capacidad_planta = 700  # <--- Subido para que supere la demanda (510)
    elif op == 3:
        materia_prima = 600
        horas_disponibles = 6
        estado_maquinaria = 80
        capacidad_planta = 300  # <--- Subido para que supere la demanda (204)
        
    return materia_prima, horas_disponibles, estado_maquinaria, capacidad_planta


