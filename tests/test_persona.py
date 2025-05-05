import allure
from db.DatabaseConnection import get_db_connection
from db.querys import UserQueries

@allure.title("Se verifica que existan personas en la Base de Datos")
def test_buscar_personas():
    personas = UserQueries.traer_personas()
    assert len(personas) > 0, "¡La query no devolvió ningún registro!"