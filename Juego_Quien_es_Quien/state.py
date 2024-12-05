import reflex as rx
import random

class State(rx.State):

    # Lista de personajes y sus características
    personajes = [{"nombre": "Susan", "color pelo": "blanco", "ojos" : "marrones", "nariz": "pequeña", "genero": "mujer", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Claire", "color pelo": "rojo", "ojos" : "marrones", "nariz": "pequeña", "genero": "mujer", "gafas": True, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "David", "color pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": True, "gorro": False},
{"nombre": "Anne", "color pelo": "marrón", "ojos" : "marrones", "nariz": "grande", "genero": "mujer", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Robert", "color pelo": "marrón", "ojos" : "azules", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Anita", "color pelo": "amarillo", "ojos" : "azules", "nariz": "pequeña", "genero": "mujer", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Joe", "color pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": True, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "George", "color pelo": "blanco", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "Bill", "color pelo": "rojo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": False, "barba": True, "gorro": False},
{"nombre": "Alfred", "color pelo": "rojo", "ojos" : "azules", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Max", "color pelo": "marron", "ojos" : "marrones", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Tom", "color pelo": "marron", "ojos" : "azules", "nariz": "pequeña", "genero": "hombre", "gafas": True, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Alex", "color pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Sam", "color pelo": "blanco", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": True, "bigotes": False, "pelo": False, "barba": False, "gorro": False},
{"nombre": "Richard", "color pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": False, "barba": True, "gorro": False},
{"nombre": "Paul", "color pelo": "blanco", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": True, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Maria", "color pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "mujer", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "Frans", "color pelo": "rojo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Herman", "color pelo": "rojo", "ojos" : "marrones", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": False, "barba": False, "gorro": False},
{"nombre": "Bernard", "color pelo": "marron", "ojos" : "marrones", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "Philip", "color pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": True, "gorro": False},
{"nombre": "Eric", "color pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "Charles", "color pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Peter", "color pelo": "blanco", "ojos" : "azules", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False}
]
    # Estado inicial del juego
    personaje_oculto = random.choice(personajes)
    mensaje = "Haz una pregunta para descubrir el personaje oculto."
    #intentos = 0
    ganador = False

    # Responder a una pregunta
    def responder_pregunta(self, pregunta: str):
        if self.ganador:
            self.mensaje = "¡Ya has ganado!"
            return
       
        self.intentos += 1
        if "color pelo" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["color pelo"] else "No"
        elif "ojos" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["ojos"] else "No"
        elif "nariz" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["nariz"] else "No"
        elif "genero" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["genero"] else "No"
        elif "gafas" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["gafas"] else "No"
        elif "bigotes" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["bigotes"] else "No"
        elif "pelo" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["pelo"] else "No"
        elif "barba" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["barba"] else "No"
        elif "gorro" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["gorro"] else "No"
        else:
            respuesta = "No entiendo la pregunta."

        self.mensaje = f"Respuesta: {respuesta}"

    '''# Adivinar el personaje
    def adivinar_personaje(self, nombre: str):
        if self.personaje_oculto["nombre"].lower() == nombre.lower():
            self.ganador = True
            self.mensaje = f"¡Correcto! El personaje oculto es {self.personaje_oculto["nombre"]}."
        else:
            self.mensaje = f"No, {nombre} no es el personaje oculto. Intenta de nuevo."
'''

    '''# Enviar pregunta.
    def enviar_pregunta(self):
        self.personaje_oculto = random.choice(self.personajes)
        self.mensaje = "Enviar pregunta"
        self.intentos = 0
        self.ganador = False'''


'''class State(rx.State):
    def __init__(self, value, text=""):
    value = str = ""
    text = str = ""
    ganador: bool = False
    carta_a_adivinar= str = random.choice(personajes)
    intentos: int = 0
    cartas_disponibles: list = personajes

    def responder_pregunta(self):
        """Procesa la pregunta ingresada por el usuario."""
        print(f"Pregunta recibida: {self.value}")
        self.intentos +=0
        self.intentos +=1


        if self.value.lower() == self.carta_a_adivinar.lower():
            self.ganador = True
            self.text = f"¡Correcto! Has adivinado en {self.intentos} intentos."
        else:
            self.text = f"Respuesta incorrecta. Intenta de nuevo."

        # Notificar a Reflex de los cambios en el estado
        
        return rx.update_state()


    def responder_pregunta(self, pregunta: str):
        if self.ganador:
           return rx.text("¡Ya has ganado! Reinicia el juego para jugar de nuevo."  )  

    # Inicializamos el estado con valores predeterminados
class Juego_Quien_es_Quien(rx.Component):
    def render(self):
        return rx.text("¡El juego ha comenzado!")


     # Aquí vamos a manejar el estado de la carta a adivinar y demás
    def on_mount(self):
        self.state = {
            "carta_a_adivinar": random.choice(personajes),
            "cartas_disponibles": personajes,
            "intentos": 0
        }
        return rx.text(f"Carta a adivinar: {self.state['carta_a_adivinar']}")

# Definimos cómo se maneja el ciclo de vida del juego y su interacción
app = Juego_Quien_es_Quien()
app.render()'''
    
    
