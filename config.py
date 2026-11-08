def solicitar_datos(): # Solicita el nombre de la planta y del supervisor
    print(" Simulador de gestion y produccion gcpp ")
    nombre_planta = str(input(" Ingrese el nombre de la planta: "))
    nombre_supervisor = str(input(" Ingrese el nombre del supervisor: "))
    return nombre_planta, nombre_supervisor

def elegir_escenario(): # Solicita al usuario a elegir un escenario
    print(" Seleccione el escenario de produccion ")
    print("1. Escenario 1 - Produccion estable ")
    print("2. Escenario 2 - Alta demanda ")
    print("3. Escenario 3 - Produccion critica ")
    
    op = int(input( " Escriba el numero correspondiente para el escenario: "))
    while op < 1 or op > 3: # Evita que el usuario utilice un numero invalido
        try:
            op = int(input(" Elija 1, 2 o 3: "))
            if op < 1 or op > 3:
                print(" Opcion no valida, intente de nuevo ")
        except ValueError:
            print(" Error, debe ingresar un numero entero ")
            
    return op

def cargar_variables(op): # Modifica variables dependiendo del escenario
    if op == 1:
        materia_prima = 1000
        horas_disponibles = 40
        estado_maquinaria = 100
        capacidad_planta = 200
    elif op == 2:
        materia_prima = 1200
        horas_disponibles = 35
        estado_maquinaria = 100
        capacidad_planta = 300
    else:
        materia_prima = 600
        horas_disponibles = 30
        estado_maquinaria = 80
        capacidad_planta = 120
        
    return materia_prima, horas_disponibles, estado_maquinaria, capacidad_planta

nombre_planta, nombre_supervisor = solicitar_datos()
opcion = elegir_escenario()
cargar_variables(opcion)