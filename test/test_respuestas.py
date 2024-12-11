import pytest

from juego_Quien_es_Quien.state import respuesta

def test_respuesta():
    assert respuesta in [("Susan", "blanco", "Si"),
                           ("Susan", "negro", "No"),
                           ("Susan", "barba", "No"),
                           ("David", "rubio", "Si"),
                           ("David", "¿Es pelirrojo?", "No"),
                           ("David", "Vallecas", "No sé cómo responder a eso"),
                           ("David", "5429875", "No sé cómo responder a eso")
                           ]