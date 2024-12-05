#Casos de prueba para mostrar el tablero

def test_tablero_muestra_todas_las_cartas():
    cartas = ["personajes"]
    tablero = mostrar_tablero(cartas)
    assert all(carta in tablero for carta in cartas), "No todas las cartas están en el tablero."

