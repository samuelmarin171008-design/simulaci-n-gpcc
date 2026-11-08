Simulación GCPP - Proyecto 1

## Descripción
Módulo de simulación de gestión y control de procesos productivos (GCPP) desarrollado en Python.

## Integrantes
_Samuel Marín
_Milcelis Del Valle
_Adrian Torres
_Angelo Sanchez
_Nelson Briceño

### Trabajos Correspondientes:
## Samuel Marin

# Configuración inicial 
# Escenario de Producción: 
El programa deja elegir al usuario 3 opciones (produccion estable, alta demanda, produccion critica) y cada una de ellas afecta a 4 variables (materia_prima, horas_disponibles, estado_maquinaria, capacidad_planta). Su modulo se encuentra en config.py en la rama feature/planificacion

## Adrian Torres

# Planificación de producción: 
Antes de entrar en la jornada se consideran varias variables para determinar si el plan propuesto es viable de acuerdo a los recursos disponibles y el escenario elegido, dependiendo del resultado puede advertir la situación, impedir o modificar el plan, afectar alguna variable o iniciar la jornada

# Proceso de produccion (INICIO DE JORNADA):
Usar reglas matemáticas, lógica y formulas coherentes que permitan que las variables anteriores afecten el resultado. Calcular: producción obtenida, materia prima consumida, desperdicio, horas utilizadas, producción pendiente.

## Milcelis Del Valle

# Sistema de Incidencias: 
Crear 4 tipos de incidencias que sean causadas como consecuencias de la planificacion de produccion, es decir que si se ignora el aviso sobre la capacidad_planta (capacidad maxima de produccion) resulte en una incidencia. Ejemplos:
Falla de maquinaria: La maquina presenta una averia
Falta de materia prima: La cantidad de materia prima no permite continuar con el plan original
Incremento de productos defectuosos: El porcentaje de productos defectuosos aumenta
Perdida de Tiempo de produccion:

# Sistema de Decisiones:







