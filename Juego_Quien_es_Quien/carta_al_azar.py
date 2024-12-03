import reflex as rx
import random

class Juego(rx.Component):
    state = rx.State(
    carta_a_adivinar = None,
    cartas_disponibles = personajes,
    intentos = 0
    )
    def inicia_juego(self):
        self.state.carta_a_adivinar = random.choice(self.state.cartas_disponibles)
        print(f"Cartas seleccionada: {self.state.carta_a_adivinar["nombre"]}")
    def render(self):
        self.iniciar_juego()
        return rx.Text("El juego ha comenzado")
    

