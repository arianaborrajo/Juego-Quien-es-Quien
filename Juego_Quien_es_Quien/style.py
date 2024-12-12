
import reflex as rx


# Estilos comunes para preguntas y respuestas.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "50%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="1em",
    box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Establecer estilos específicos para preguntas y respuestas.
pregunta_estilo = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 4),
)
respuesta_estilo = message_style | dict(
    margin_right=chat_margin,
    background_color=rx.color("accent", 8),
)

# Estilos para la barra de acciones.
entrada_estilo = dict(
    border_width="1px",
    padding="0.5em",
    box_shadow=shadow,
    width="350px",
)
boton_estilo = dict(
    background_color=rx.color("accent", 10),
    box_shadow=shadow,
)