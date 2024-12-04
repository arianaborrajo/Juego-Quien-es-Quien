def filtrar_cartas(self, atributo, valor) :
    self.state.cartas_disponibles = [
        p for p in self.state.cartas_disponibles if p[atributo] == valor]
    self.state.intentos +=1

def render(self):
    self.iniciar_juego()
    return rx.Box(
            rx.Text("Tablero de personajes"),
            rx.Grid(...),
            rx.Box(
                rx.Text("Filtra las cartas ingresando características"),
                rx.Input(placeholder="Atributo (e.g., gafas, pelo, sombrero)", id="atributo"),
                rx.Input(placeholder="Valor(True/False o color)", id="valor"),
                rx.Button(
                    "Filtrar",
                    on_click=lambda:
self.filtrar_cartas(
                        rx.get_value("atributo"),
                        eval (rx.get_value("valor"))
                    )
                )
            )
        )