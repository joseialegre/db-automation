import allure
import pandas as pd
from db.DatabaseConnection import get_db_connection
from db.DatabaseStep import DatabaseStep


class UserQueries:

    @staticmethod
    @allure.step("Se buscan las personas en la base de datos",)
    def traer_personas():
        query: str = 'SELECT TOP 10 * FROM saldos'
        allure.attach(query, name="Consulta SQL", attachment_type=allure.attachment_type.TEXT)
        return DatabaseStep.executeQuery(query)