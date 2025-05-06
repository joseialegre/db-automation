import allure
from db.querys import UserQueries

@allure.suite("Validaciones de Personas")
@allure.tag("personas")
@allure.title("Se verifica que existan personas en la Base de Datos")
def test_buscar_personas():
    personas = UserQueries.traer_personas()
    assert len(personas) > 0, "¡La query no devolvió ningún registro!"