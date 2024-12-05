#Casos de prueba para mostrar el tablero

def test_tablero_muestra_todas_las_cartas():
    cartas = ["personajes"]
    tablero = mostrar_tablero(cartas)
    assert all(carta in tablero for carta in cartas), "No todas las cartas están en el tablero."

def test_formato_tablero():
    cartas = ["personajes"]
    tablero = mostrar_tablero(cartas)
    filas = len(tablero)
    columnas = len(tablero[0]) if filas > 0 else 0
    assert filas == 4 and columnas == 6, "El tablero no tiene el formato esperado."

def test_tablero_vacio():
    cartas = []
    tablero = mostrar_tablero(cartas)
    assert tablero == [], "El tablero no debería contener elementos si no hay cartas."