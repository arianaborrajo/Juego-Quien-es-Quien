#Casos de prueba para seleccionar una carta al azar

def test_una_sola_carta():
    personajes = ["personaje1"]
    personaje_oculto = seleccionar_personaje(personaje)
    assert seleccionar_carta == "personaje1", "No seleccionó la única carta disponible."

def test_seleccionar_carta_aleatoria():
    carta_seleccionada = seleccionar_carta(personajes)
    assert carta_seleccionada in personajes, "La carta seleccionada no pertenece al conjunto."