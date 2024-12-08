class Juego(rx.Component):
    def render(self):
        self.iniciar_juego()
        return rx.Box(rx.Text("Tablero de personajes:"),rx.Grid(children = [rx.Box(rx.Text (f"Nombre: {p['nombre']}"),
                    rx.Text(f"Gafas: {'Sí' if p['gafas'] else 'No'}"),
                    rx.Text(f"Pelo:{p['pelo']}"),
                    rx.Text(f"Sombrero: {'Sí' if p['sombrero'] else 'No'}"), border = "1px solid black", padding = "10px", marging = "5px",)
                    for p in self.state.cartas_disponibles],template_columns = "repeat(auto-fit, minmax(150px, 1fr))", gap = "10px"))