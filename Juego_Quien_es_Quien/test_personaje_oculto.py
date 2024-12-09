import pytest

from .state import personaje_oculto

def test_personaje_oculto():
    assert personaje_oculto() in ["Susan", "Claire", "David", "Anne", "Robert", 
                                  "Anita", "Joe", "George", "Bill", "Alfred", 
                                  "Max", "Tom", "Alex", "Sam", "Richard", "Paul", 
                                  "Maria", "Frans", "Herman", "Bernard", "Philip", 
                                  "Eric", "Charles", "Peter"]