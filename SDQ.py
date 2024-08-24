class SDQCalculator:
    def __init__(self):
        self.nombre_participante = ""
        self.edad_participante = ""
        self.respuestas = {}
        self.resultados = {}

    def ingresar_datos_participante(self):
        """
        Solicita el nombre y la edad del participante.
        """
        self.nombre_participante = input("Ingrese el nombre completo del participante: ")
        self.edad_participante = input("Ingrese la edad del participante (o 'NA' si no se conoce): ")

    def ingresar_respuestas(self):
        """
        Solicita las respuestas para cada uno de los 25 ítems.
        """
        print("\nPor favor, ingrese las respuestas para los 25 ítems del SDQ-CAS.")
        print("Responda '1' para 'not true', '2' para 'somewhat true', '3' para 'certainly true'.\n")

        for i in range(1, 26):
            while True:
                try:
                    respuesta = int(input(f"Respuesta para el ítem {i}: "))
                    if respuesta in [1, 2, 3]:
                        self.respuestas[i] = respuesta
                        break
                    else:
                        print("Por favor, ingrese un valor válido (1, 2 o 3).")
                except ValueError:
                    print("Por favor, ingrese un número.")

    def calcular_emotional_scale(self):
        """
        Calcula la puntuación para la subescala 'Emotional Scale'.
        """
        items_emotional_scale = {
            3: {1: 0, 2: 1, 3: 2},
            8: {1: 0, 2: 1, 3: 2},
            13: {1: 0, 2: 1, 3: 2},
            16: {1: 0, 2: 1, 3: 2},
            24: {1: 0, 2: 1, 3: 2}
        }

        puntuacion = 0
        for item, valores in items_emotional_scale.items():
            respuesta = self.respuestas.get(item, 1)  # Cambiar el valor por defecto de 0 a 1 para reflejar la nueva entrada
            puntuacion += valores.get(respuesta, 0)

        return puntuacion

    def calcular_conduct_problem_scale(self):
        """
        Calcula la puntuación para la subescala 'Conduct Problem Scale'.
        """
        items_conduct_problem_scale = {
            5: {1: 0, 2: 1, 3: 2},
            7: {1: 2, 2: 1, 3: 0},
            12: {1: 0, 2: 1, 3: 2},
            18: {1: 0, 2: 1, 3: 2},
            22: {1: 0, 2: 1, 3: 2}
        }

        puntuacion = 0
        for item, valores in items_conduct_problem_scale.items():
            respuesta = self.respuestas.get(item, 1)  # Cambiar el valor por defecto de 0 a 1 para reflejar la nueva entrada
            puntuacion += valores.get(respuesta, 0)

        return puntuacion

    def calcular_hyperactivity_scale(self):
        """
        Calcula la puntuación para la subescala 'Hyperactivity Scale'.
        """
        items_hyperactivity_scale = {
            2: {1: 0, 2: 1, 3: 2},
            10: {1: 0, 2: 1, 3: 2},
            15: {1: 0, 2: 1, 3: 2},
            21: {1: 2, 2: 1, 3: 0},
            25: {1: 2, 2: 1, 3: 0}
        }

        puntuacion = 0
        for item, valores in items_hyperactivity_scale.items():
            respuesta = self.respuestas.get(item, 1)  # Cambiar el valor por defecto de 0 a 1 para reflejar la nueva entrada
            puntuacion += valores.get(respuesta, 0)

        return puntuacion

    def calcular_peer_problem_scale(self):
        """
        Calcula la puntuación para la subescala 'Peer Problem Scale'.
        """
        items_peer_problem_scale = {
            6: {1: 0, 2: 1, 3: 2},
            11: {1: 2, 2: 1, 3: 0},
            14: {1: 2, 2: 1, 3: 0},
            19: {1: 0, 2: 1, 3: 2},
            23: {1: 0, 2: 1, 3: 2}
        }

        puntuacion = 0
        for item, valores in items_peer_problem_scale.items():
            respuesta = self.respuestas.get(item, 1)  # Cambiar el valor por defecto de 0 a 1 para reflejar la nueva entrada
            puntuacion += valores.get(respuesta, 0)

        return puntuacion

    def calcular_todas_subescalas(self):
        """
        Calcula las puntuaciones para todas las subescalas y actualiza el diccionario de resultados.
        """
        self.resultados["Emotional Scale"] = self.calcular_emotional_scale()
        self.resultados["Conduct Problem Scale"] = self.calcular_conduct_problem_scale()
        self.resultados["Hyperactivity Scale"] = self.calcular_hyperactivity_scale()
        self.resultados["Peer Problem Scale"] = self.calcular_peer_problem_scale()

    def mostrar_resultados(self):
        """
        Muestra los resultados calculados para cada subescala, junto con la información del participante.
        """
        print("\nResultados de las subescalas del SDQ-CAS:")
        print(f"Nombre del participante: {self.nombre_participante}")
        print(f"Edad del participante: {self.edad_participante}\n")
        for subescala, puntuacion in self.resultados.items():
            print(f"{subescala}: {puntuacion}")
            total_puntuacion = sum(self.resultados.values())
        print(f"\nPuntuación total: {total_puntuacion}")

# Ejemplo de uso
sdq_calculator = SDQCalculator()
sdq_calculator.ingresar_datos_participante()
sdq_calculator.ingresar_respuestas()
sdq_calculator.calcular_todas_subescalas()
sdq_calculator.mostrar_resultados()
