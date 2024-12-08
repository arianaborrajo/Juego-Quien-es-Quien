import reflex as rx

from .state import State


from rxconfig import config

def index():
    return rx.center(
        rx.vstack(
            rx.heading("¿Quién es Quién?", size="2"),
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

def pyr(pregunta: str, respuesta: str) -> rx.Component:
    return rx.box(
        rx.box(pregunta, text_align="right"),
        rx.box(respuesta, text_align="left"),
        margin_y="1em"
    )

def inicio_partida() -> rx.Component:
    return rx.hstack(
        rx.button("Iniciar partida", 
                on_click=State.iniciar_partida, 
                on_blur=State.iniciar_partida,
                color_scheme="blue"),
    )

def entrada_preguntas() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.pregunta,
            placeholder="Haz una pregunta",
            on_change=State.set_pregunta,
            on_blur=State.respuesta,
        ),
        rx.button("Enviar",
                #on_click=State.respuesta,      
        ),
    )
    

def juego() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.historial_juego,
            lambda mensajes: pyr(mensajes[0], mensajes[1]),
        )
    )

def cartas() -> rx.Component:  
    return rx.grid(
        rx.foreach(
            rx.Var.range(24),
            lambda i: rx.card(State.nombre_personaje, height="10vh", width="auto"),
                    ),
                    rows="4",
                    flow="column",
                    justify="between",
                    spacing="4",
                    width="100%",
                ),
             

'''def cartas() -> rx.Component:
    return rx.grid(
        rx.foreach(
            personajes,
            #rx.Var.range(24),
            lambda carta: rx.card(
                [rx.text("nombre: {personaje['nombre']}",font_weight="bold", font_size="16px"),],
                height="15vh",  # Ajustamos la altura de las cartas
                border="1px solid #000",  # Borde de la carta
                border_radius="10px",  # Bordes redondeados
                padding="10px",  # Espaciado interno
                background_color="#f0f0f0",
                ),
        ),
        rows="4",
        flow="column",
        justify="between",
        spacing="4",
        width="100%",
    )'''

'''def cartas() -> rx.Component:
    return rx.grid(
        rx.foreach(
            rx.Var.range(24),
            lambda i: rx.card(["nombre"],height="10vh"),
                    ),
                    rows="4",
                    flow="column",
                    justify="between",
                    spacing="4",
                    width="100%",
                ),'''


app = rx.App()
app.add_page(index)
