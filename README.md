Simulación GCPP - Proyecto 1

## Descripción
Módulo de simulación de gestión y control de procesos productivos (GCPP) desarrollado en Python.

## Integrantes
_Samuel Marín
_Milcelis Del Valle
_Adrian Torres
_Angelo Sanchez
_Nelson Briceño

# Trabajos Correspondientes:
## Samuel Marin

### Configuración inicial 
### Escenario de Producción: 
El programa deja elegir al usuario 3 opciones (produccion estable, alta demanda, produccion critica) y cada una de ellas afecta a 4 variables (materia_prima, horas_disponibles, estado_maquinaria, capacidad_planta). Su modulo se encuentra en config.py en la rama feature/planificacion

### Panel de Estado: 
Después de cada jornada, decisión importante o incidencia, el programa deberá mostrar un resumen actualizado del estado de la planta. Se debe esperar a que el programa este casi completo para incorporar esta funcion. Crear modulo especifico

## Adrian Torres

### Planificación de producción: 
Antes de entrar en la jornada se consideran varias variables para determinar si el plan propuesto es viable de acuerdo a los recursos disponibles y el escenario elegido, dependiendo del resultado puede advertir la situación, impedir o modificar el plan, afectar alguna variable o iniciar la jornada. Su modulo se encuentra incorporado ya en la rama main

### Proceso de produccion (INICIO DE JORNADA):
Usar reglas matemáticas, lógica y formulas coherentes que permitan que las variables anteriores afecten el resultado. Calcular: producción obtenida, materia prima consumida, desperdicio, horas utilizadas, producción pendiente.

## Milcelis Del Valle (Crear una rama aparte)

### Sistema de Incidencias: 
Crear 4 tipos de incidencias que sean causadas como consecuencias de la planificacion de produccion, es decir que si se ignora el aviso sobre la capacidad_planta (capacidad maxima de produccion) resulte en una incidencia. Ejemplos:
Falla de maquinaria: La maquina presenta una averia.
Falta de materia prima: La cantidad de materia prima no permite continuar con el plan original.
Incremento de productos defectuosos: El porcentaje de productos defectuosos aumenta.
Perdida de Tiempo de produccion:

### Sistema de Decisiones:
Cada incidencia debe tener al menos tres alternativas de decisiones, y estas deberán tener consecuencias dentro de las variables, sean positivas o negativas, estas deben afectar una o mas variables. Ejemplo:

Opcion A Reparacion Inmediata: Aumento del costo, reduccion del tiempo perdido, recuperacion de la capacidad productiva

Opcion B Continuar Produccion: Menor costo inmediato, mayor cantidad de productos defectuosos, reduccion de la calidad

### Sistema de Mantenimiento: (FINALIZACION DE LA JORNADA)
El usuario debe decidir si se realiza o no una accion de mantenimiento. Estas decisiones deben afectar variables de produccion, aunque estas solo tendran efecto en las jornadas siguientes, es decir que si no se hace mantenimiento a la maquina en 3 jornadas, en la 4 fallara y supondra un aumento del coste total. Debe tener al menos:

Estado de la maquina, mantenimiento preventivo, mantenimiento correctivo, tiempo de mantenimiento, costo de mantenimiento

## Angelo Sanchez

### Control de Calidad:
Establecer reglas para cuando una producción es aceptable o presenta problemas despues de cada jornada, debe incluir: Unidades producidas, unidades defectuosas, porcentaje de defectos, pocentaje de calidad

### Indicadores del Proceso (Las formulas deben estar documentadas en el README):
Calcular:
Cumplimiento de produccion: Relacion entre la produccion planificada y la realizada

Calidad: Relacion entre unidades aceptadas y producidas

Eficiencia: Indicador definido por el equipo para comparar el rendimiento obtenido con las condiciones previstas

Desperdicio: Cantidad de material perdido durante el proceso

Tiempo Perdido: Cantidad de horas no utilizadas debido a incidencias, mantenimiento u otras situaciones

### Sistema de Costos:
Incorporar un calculo básico del costo acumulado de la jornada donde incluya:

Costo de materia prima, costo de mantenimiento, costo asociado al tiempo perdido, penalización de productos defectuosos

No es necesario utilizar dinero real ni base de datos, el equipo debe decidir las reglas o formulas necesarias para el calculo.

## Nelson Briceño:
### Evaluacion de cada Jornada: 
Al finalizar cada jornada se deberan analizar las condiciones actuales y determinar su estado. Por ejemplo:

Produccion: Cumplida

Calidad: Aceptable

Desperdicio: Controlado

Eficiencia: Alta

JORNADA SUPERADA

(Agregar tambien estados negativos)

### Sistema para la siguiente jornada
Crear un ciclo for o while para avanzar hasta la siguiente jornada hasta cumplir las 5

### Resultado Final de la evaluacion (Recomiendo mirar el ejemplo en el PDF del profe)
Después de completar las cinco jornadas, el programa deberá presentar un informe final. Como mínimo:

Producción total planificada

Producción total realizada

Producción pendiente

Total de productos defectuosos

Desperdicio acumulado

Horas utilizadas

Horas perdidas

Calidad final

Eficiencia final

Costo acumulado

Resultado general de la planta

El resultado dependerá de todas las decisiones tomadas durante la simulación

### Múltiples Resultados finales
La simulación deberá tener distintos resultados finales como: Cumplimiento satisfactorio del plan, cumplimiento parcial, incumplimiento del plan, resultado critico por problemas de calidad, resultado critico por falta de recursos. Las condiciones para cada resultado deben de estar definidas y tener su lógica correspondiente

### Reinicio de la simulacion
Al finalizar la simulación el programa deberá iniciar una nueva sin cerrar la aplicación, dando la opción de Si/No. Esta funcionalidad debe ser añadida mediante ciclos

# DIAGRAMA DE FLUJO
<img width="804" height="455" alt="Captura de pantalla 2026-11-07 143011" src="https://github.com/user-attachments/assets/e5c73879-88fd-4e43-9414-a6af1106dc81" />

<img width="802" height="459" alt="Captura de pantalla 2026-11-07 143032" src="https://github.com/user-attachments/assets/66b06426-8e22-4348-9661-54c05f8f2cab" />

<img width="782" height="448" alt="Captura de pantalla 2026-11-07 143046" src="https://github.com/user-attachments/assets/d362b332-7eb8-4732-9764-05932f152b35" />

<img width="801" height="446" alt="Captura de pantalla 2026-11-07 143057" src="https://github.com/user-attachments/assets/2c14870d-f51a-442a-862b-06160d91b088" />















