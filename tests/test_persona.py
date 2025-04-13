import allure
from db.connection import get_db_connection
from db.querys import UserQueries

def test_query_personas_trae_datos():
    # corregir llamada a bd
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM persona")
        personas = cursor.fetchall()
    assert len(personas) > 0, "¡La query no devolvió ningún registro!"

@allure.title("Se verifica que existan personas en la Base de Datos")
def test_buscar_personas():
    personas = UserQueries.traer_personas()
    assert len(personas) > 0, "¡La query no devolvió ningún registro!"

def test_se_busca_persona_especifica():
    # corregir llamada a bd
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PERSONA WHERE CUIT = 1")
        personas = cursor.fetchall()
    assert len(personas) > 0, "La query no trajo na..."
