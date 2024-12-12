import reflex as rx

from .state import State

from juego_quien_es_quien import style

from rxconfig import config

def index():
    return rx.center(
        rx.vstack(
            rx.heading("¿Quién es Quién?", size="5"),
            inicio_partida(),
            rx.text(State.mensaje, font_size="lg", margin_bottom="20px"),
            cartas(),
            juego(),
            entrada_preguntas(),
            align="center",
            ),
            padding="20px",
            border="1px solid black",
            border_radius="10px",
            width="100%",
            height="100%",
    )

def inicio_partida() -> rx.Component:
    return rx.hstack(
        rx.button("Iniciar partida", 
                on_click=State.iniciar_partida, 
                color_scheme="blue"),
    )

def cartas() -> rx.Component:
    return rx.grid(
        rx.foreach(
            State.nombre,
            lambda i: rx.card(
                rx.image(src=f"{i}.png", height="20vh"),)
                    ),
                    rows="3",
                    flow="column",
                    justify="between",
                    spacing="4",
                    width="100%",
                ),

def pyr(pregunta: str, respuesta: str) -> rx.Component:
    return rx.box(
        rx.box(pregunta, style=style.pregunta_estilo, text_align="right"),
        rx.box(respuesta, style=style.respuesta_estilo, text_align="left"),
        margin_y="1em", width="100%"
        
    )

def juego() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.historial_juego,
            lambda mensajes: pyr(mensajes[0], mensajes[1]),
        )
    )    
         
def entrada_preguntas() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.pregunta,
            placeholder="Haz una pregunta",
            on_change=State.set_pregunta,
            style=style.entrada_estilo,
        ),
        rx.button("Enviar",
                  on_click=State.respuesta,
                  style=style.boton_estilo     
        ),
    )

        
       
app = rx.App()
app.add_page(index)
