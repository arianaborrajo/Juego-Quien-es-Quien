#Casos de prueba para seleccionar una carta al azar

def test_una_sola_carta():
    personajes = ["personaje1"]
    personaje_oculto = seleccionar_personaje(personaje)
    assert seleccionar_carta == "personaje1", "No seleccionó la única carta disponible."

