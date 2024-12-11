import pytest

from juego_Quien_es_Quien.state import State

def test_personaje_oculto():
    estado = State()
    estado.elegir_personaje()
    assert estado.personaje_oculto["nombre"] in ["Susan", "Claire", "David", "Anne", "Robert", 
                                  "Anita", "Joe", "George", "Bill", "Alfred", 
                                  "Max", "Tom", "Alex", "Sam", "Richard", "Paul", 
                                  "Maria", "Frans", "Herman", "Bernard", "Philip", 
                                  "Eric", "Charles", "Peter"]