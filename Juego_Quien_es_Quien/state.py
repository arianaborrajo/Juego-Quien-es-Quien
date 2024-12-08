import reflex as rx

import random

import asyncio


class State(rx.State):
    

# Lista de personajes y sus características
    personajes = [{"nombre": "Susan", "color_pelo": "blanco", "ojos" : "marrones", "nariz": "pequeña", "genero": "mujer", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Claire", "color_pelo": "rojo", "ojos" : "marrones", "nariz": "pequeña", "genero": "mujer", "gafas": True, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "David", "color_pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": True, "gorro": False},
{"nombre": "Anne", "color_pelo": "marrón", "ojos" : "marrones", "nariz": "grande", "genero": "mujer", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Robert", "color_pelo": "marrón", "ojos" : "azules", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Anita", "color_pelo": "amarillo", "ojos" : "azules", "nariz": "pequeña", "genero": "mujer", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Joe", "color_pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": True, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "George", "color_pelo": "blanco", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "Bill", "color_pelo": "rojo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": False, "barba": True, "gorro": False},
{"nombre": "Alfred", "color_pelo": "rojo", "ojos" : "azules", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Max", "color_pelo": "marron", "ojos" : "marrones", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Tom", "color_pelo": "marron", "ojos" : "azules", "nariz": "pequeña", "genero": "hombre", "gafas": True, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Alex", "color_pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Sam", "color_pelo": "blanco", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": True, "bigotes": False, "pelo": False, "barba": False, "gorro": False},
{"nombre": "Richard", "color_pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": False, "barba": True, "gorro": False},
{"nombre": "Paul", "colo_pelo": "blanco", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": True, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Maria", "color_pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "mujer", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "Frans", "color_pelo": "rojo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Herman", "color_pelo": "rojo", "ojos" : "marrones", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": False, "barba": False, "gorro": False},
{"nombre": "Bernard", "color_pelo": "marron", "ojos" : "marrones", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "Philip", "color_pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": True, "gorro": False},
{"nombre": "Eric", "color_pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
{"nombre": "Charles", "color_pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": True, "barba": False, "gorro": False},
{"nombre": "Peter", "color_pelo": "blanco", "ojos" : "azules", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False}
]
    personaje_oculto = random.choice(personajes)
    mensaje = ""
    ganador = False
    intentos = 0
    juego_iniciado = False
    pregunta: str
    historial_juego: list[tuple[str, str]]
    personajes: list[dict] = []
    
    def iniciar_partida(self):
        if self.personaje_oculto: 
            self.mensaje = "¡El Juego Ha Comenzado!"
            self.ganador = False
            return
        
        self.juego_iniciado : False
        self.intentos: 0
    

    @rx.event
    async def respuesta(self, pregunta: str):
        if self.ganador:
            self.mensaje = "¡Ganaste!"
            return
        
        self.intentos += 1
        if self.personaje_oculto["ojos"].lower() == pregunta.lower():
            respuesta = "Sí"

        elif self.personaje_oculto["nombre"].lower() == pregunta.lower():
            respuesta = "Sí"
            self.mensaje = "¡Ganaste!"

        elif self.personaje_oculto["color_pelo"].lower() == pregunta.lower():
            respuesta = "Sí"

        elif self.personaje_oculto["nariz"].lower() == pregunta.lower():
            respuesta = "Sí"

        elif self.personaje_oculto["genero"].lower() == pregunta.lower():
            respuesta = "Sí"

        elif pregunta not in self.personaje_oculto: respuesta = "No" 

        elif "gafas" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["gafas"] else "No"

        elif "bigotes" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["bigotes"] else "No"

        elif "pelo" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["pelo"] else "No"

        elif "barba" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["barba"] else "No"

        elif "ojos" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["ojos"] else "No"

        elif "gorro" in pregunta:
            respuesta = "Sí" if self.personaje_oculto["gorro"] else "No"

             
        self.historial_juego.append((self.pregunta, respuesta))
        self.pregunta = "" # Limpiar la pregunta

    # Historial de pyr
        for i in range(len(respuesta)):
            await asyncio.sleep(0.1)
            self.historial_juego[-1] = (
            self.historial_juego[-1][0],
            respuesta[: i + 1],
        )
        yield

