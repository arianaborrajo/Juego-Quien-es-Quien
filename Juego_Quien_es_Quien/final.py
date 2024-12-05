def adivinar_carta(self, nombre):
    if nombre == self.state.carta_a_adivinar['nombre']:
        return "¡Ganaste! Adivinaste la carta."
    else:
        return f"Perdiste. La carta era {self.state.carta_a_adivinar['nombre']}."
    
def render(self):
    self.iniciar_juego()
    if len(self.state.cartas_disponibles) <= 3:
        return rx.Box(rx.Text("¿Cuál es tu elección?"),rx.Input(placeholder="Nombre de la carta", id="eleccion"), rx.Button("Adivinar", on_click = lambda: rx.Text(self.adivinar_carta(rx.get_value("elección")))))
   
    