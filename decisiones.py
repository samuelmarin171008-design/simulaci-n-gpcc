from decisiones import SistemaDecisiones

# Variables compartidas de produccion
variables_produccion = {
    "costo_total": 0,
    "tiempo_perdido": 0,
    "capacidad_disponible": 100,
    "materia_prima": 100,
    "productos_defectuosos": 0,
    "calidad": 100
}

# Crear el sistema de decisiones
sistema_decisiones = SistemaDecisiones(variables_produccion)

# Probar una incidencia
sistema_decisiones.mostrar_opciones("Falla de maquinaria")
