"""Programa principal del Simulador GCPP.

Solo coordina el flujo general: configuracion inicial, simulacion de las
jornadas y reinicio. La logica esta repartida en los demas modulos.
"""

import config
import simulacion


def main():
    """Repite la simulacion mientras el usuario responda 'Si' al reinicio."""
    nueva_simulacion = True
    while nueva_simulacion:
        config.solicitar_datos()
        escenario = config.elegir_escenario()
        simulacion.ejecutar_simulacion(escenario)
        nueva_simulacion = simulacion.preguntar_nueva_simulacion()
    print("\nGracias por usar el simulador. Hasta pronto.")


if __name__ == "__main__":
    main()
