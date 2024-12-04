
def hacer_pregunta(pregunta, respuesta):
    global personajes
    personajes = [p for p in personajes if p[pregunta] == respuesta]

import reflex as rx
class QuienEsQuien (rx.Component):
    state = rx.State(personajes=personajes, pregunta_actual="",respuestas=[])

    def adivinar(self):
        pass
