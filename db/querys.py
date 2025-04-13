import allure
from allure_commons.mapping import allure_tag_sep
from allure_pytest.utils import allure_description

from db.connection import get_db_connection

class UserQueries:
    @staticmethod
    def get_all_users():
        return "SELECT * FROM Persona"

    @staticmethod
    @allure.step("Se buscan las personas en la base de datos")
    def traer_personas():
        query = "SELECT * FROM persona"
        with get_db_connection() as conn:
            return UserQueries.ejecutar_consulta(query, conn)

    @staticmethod
    @allure.step("Ejecutando consulta SQL: {query}")
    def ejecutar_consulta(query, conn):
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
