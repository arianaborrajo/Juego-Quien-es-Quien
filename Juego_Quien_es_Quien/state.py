import reflex as rx

import random




class State(rx.State):


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
        {"nombre": "Paul", "color_pelo": "blanco", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": True, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
        {"nombre": "Maria", "color_pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "mujer", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
        {"nombre": "Frans", "color_pelo": "rojo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False},
        {"nombre": "Herman", "color_pelo": "rojo", "ojos" : "marrones", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": False, "barba": False, "gorro": False},
        {"nombre": "Bernard", "color_pelo": "marron", "ojos" : "marrones", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
        {"nombre": "Philip", "color_pelo": "marron", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": True, "gorro": False},
        {"nombre": "Eric", "color_pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": True},
        {"nombre": "Charles", "color_pelo": "amarillo", "ojos" : "marrones", "nariz": "pequeña", "genero": "hombre", "gafas": False, "bigotes": True, "pelo": True, "barba": False, "gorro": False},
        {"nombre": "Peter", "color_pelo": "blanco", "ojos" : "azules", "nariz": "grande", "genero": "hombre", "gafas": False, "bigotes": False, "pelo": True, "barba": False, "gorro": False}
        ]

    nombre = ["Susan", "Claire","David","Anne", "Robert", "Anita", "Joe", "George", "Bill", "Alfred", "Max", "Tom", "Alex", "Sam", 
                    "Richard", "Paul", "Maria", "Frans", "Herman", "Bernard", "Philip", "Eric", "Charles", "Peter"]
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
        
    

   
    def respuesta(self):
        if self.ganador:
            self.mensaje = "¡Ganaste!"
            return
        
        self.intentos += 1
        if self.personaje_oculto["ojos"].lower() == self.pregunta.lower():
            respuesta = "Sí"

        elif self.personaje_oculto["nombre"].lower() == self.pregunta.lower():
            respuesta = "Sí"
            self.mensaje = "¡Ganaste!"

        elif self.personaje_oculto["color_pelo"].lower() == self.pregunta.lower():
            respuesta = "Sí"

        elif self.personaje_oculto["nariz"].lower() == self.pregunta.lower():
            respuesta = "Sí"

        elif self.personaje_oculto["genero"].lower() == self.pregunta.lower():
            respuesta = "Sí"

        elif self.pregunta not in self.personaje_oculto: respuesta = "No" 

        elif "gafas" in self.pregunta:
            respuesta = "Sí" if self.personaje_oculto["gafas"] else "No"

        elif "bigotes" in self.pregunta:
            respuesta = "Sí" if self.personaje_oculto["bigotes"] else "No"

        elif "pelo" in self.pregunta:
            respuesta = "Sí" if self.personaje_oculto["pelo"] else "No"

        elif "barba" in self.pregunta:
            respuesta = "Sí" if self.personaje_oculto["barba"] else "No"

        elif "gorro" in self.pregunta:
            respuesta = "Sí" if self.personaje_oculto["gorro"] else "No"

             
        self.historial_juego.append((self.pregunta, respuesta))
        self.pregunta = "" 

    
    


