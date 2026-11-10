class SistemaMantenimiento:

    def _init_(self):
        # Estado inicial de la maquina
        self.estado_maquina = 100

        # Contador de jornadas sin mantenimiento
        self.jornadas_sin_mantenimiento = 0

        # Variables de mantenimiento
        self.tiempo_mantenimiento = 0
        self.costo_mantenimiento = 0
        self.mantenimiento_preventivo = 0
        self.mantenimiento_correctivo = 0

        # Indica si la maquina esta averiada
        self.maquina_averiada = False

    def finalizar_jornada(self):
        print("\n--- MANTENIMIENTO AL FINALIZAR LA JORNADA ---")
        print("Estado de la maquina:", self.estado_maquina)

        print("\n¿Desea realizar mantenimiento?")
        print("1. Si, mantenimiento preventivo")
        print("2. No realizar mantenimiento")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            self.realizar_mantenimiento()
        elif opcion == "2":
            self.jornadas_sin_mantenimiento += 1
            print("No se realizo mantenimiento.")

            if self.jornadas_sin_mantenimiento >= 3:
                self.maquina_averiada = True
                print("ADVERTENCIA: La maquina ha fallado.")
                self.estado_maquina = 0
        else:
            print("Opcion no valida.")

    def realizar_mantenimiento(self):
        self.jornadas_sin_mantenimiento = 0

        self.mantenimiento_preventivo += 1
        self.tiempo_mantenimiento += 2
        self.costo_mantenimiento += 100

        self.estado_maquina = min(100, self.estado_maquina + 30)

        self.maquina_averiada = False

        print("\nMantenimiento preventivo realizado.")
        print("Estado de la maquina:", self.estado_maquina)
        print("Costo de mantenimiento:", self.costo_mantenimiento)
        print("Tiempo de mantenimiento:", self.tiempo_mantenimiento)

    def realizar_mantenimiento_correctivo(self):
        self.mantenimiento_correctivo += 1
        self.tiempo_mantenimiento += 5
        self.costo_mantenimiento += 250

        self.estado_maquina = 100
        self.maquina_averiada = False
        self.jornadas_sin_mantenimiento = 0

        print("\nMantenimiento correctivo realizado.")
        print("Costo de mantenimiento:", self.costo_mantenimiento)
        print("Tiempo de mantenimiento:", self.tiempo_mantenimiento)

    def mostrar_estado(self):
        print("\n--- ESTADO ACTUAL DE LA MAQUINA ---")
        print("Estado:", self.estado_maquina)
        print("Jornadas sin mantenimiento:",
              self.jornadas_sin_mantenimiento)
        print("Mantenimientos preventivos:",
              self.mantenimiento_preventivo)
        print("Mantenimientos correctivos:",
              self.mantenimiento_correctivo)
        print("Costo total:", self.costo_mantenimiento)
        print("Tiempo total:", self.tiempo_mantenimiento)
        print("Maquina averiada:", self.maquina_averiada)