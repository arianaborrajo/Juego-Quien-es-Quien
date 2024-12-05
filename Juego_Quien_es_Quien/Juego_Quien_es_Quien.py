import sys
import os

# Añadir la ruta del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import reflex as rx
#from rxconfig import config
from .state import State

state = State(value="Estado inicial")
#class State(rx.State):
 #   """The app state."""

  #  ...


def index():
    return rx.box(
        rx.input(
            placeholder="Haz una pregunta (¿Tiene gafas? ¿Usa gorro?)",
            value=State.value,  # Se conecta al estado
            on_blur=State.responder_pregunta,  # Llama al método responder_pregunta
        ),
        rx.text(State.text),  # Muestra el mensaje del estado
    )           
    

    #return rx.center(
     #   rx.vstack(
      #      rx.heading("¿Quién es Quién?", size="2"),
       #     rx.text(state.text, font_size="lg", margin_bottom="20px"),
            
            # Campo para hacer preguntas
        #    rx.hstack(
        #        rx.input(
        #            placeholder="Haz una pregunta (¿Tiene gafas? ¿Usa gorro?)",
        #            on_blur=state.responder_pregunta,
        #        ),
                #rx.button("Enviar pregunta", on_click=lambda: rx.update(State.some_value)),
        #    ),

            # Campo para adivinar el personaje
           # rx.hstack(
            #    rx.input(
             #       placeholder="Adivina el personaje (Ana, Luis, etc.)",
              #      on_blur=state.adivinar_personaje,
               # ),
                #rx.button("Adivinar", on_click=lambda: None),
            #),

            # Botón para reiniciar el juego
           # rx.button("Reiniciar Juego", on_click=state.reiniciar_juego, color_scheme="blue"),
        #),
        #padding="20px",
        #border="1px solid black",
        #border_radius="10px",
        #width="50%",
        #height="50%",
    #)

app = rx.App()
app.add_page(index)





#def index() -> rx.Component:
    # Welcome Page (Index)
 #   return rx.container(
  #      rx.color_mode.button(position="top-right"),
   #     rx.vstack(
    #        rx.heading("Welcome to Reflex!", size="9"),
     #       rx.text(
      #          "Get started by editing ",
       #         rx.code(f"{config.app_name}/{config.app_name}.py"),
        #        size="5",
         #   ),
          #  rx.link(
           #     rx.button("Check out our docs!"),
            #    href="https://reflex.dev/docs/getting-started/introduction/",
             #   is_external=True,
            #)
            #spacing="5",
            #justify="center",
            #min_height="85vh",
        #),
        #rx.logo(),
    #)


#app = rx.App()
#app.add_page(index)
