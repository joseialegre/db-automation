import os
import allure
from db.DatabaseStep import DatabaseStep


class UserQueries:

    @staticmethod
    @allure.step("Se buscan las personas en la base de datos",)
    def traer_personas():
        query = UserQueries.readSQLFile("SQLFile1")
        allure.attach(query, name="Consulta SQL", attachment_type=allure.attachment_type.TEXT)
        return DatabaseStep.executeQuery(query)

    @staticmethod
    @allure.step("Se buscan saldos y cre_saldos")
    def saldos_y_cresaldos():
        query = UserQueries.readSQLFile("Saldos/saldos_cresaldos_sin_referencia")
        allure.attach(query, name="Consulta SQL", attachment_type=allure.attachment_type.TEXT)
        return DatabaseStep.executeQuery(query)

    @staticmethod
    @allure.step("Se buscan referencias nulas de sucursales")
    def sucursales_saldos():
        query = UserQueries.readSQLFile("Sucursales/saldos_sucursales_sin_referencia")
        allure.attach(query, name="Consulta SQL", attachment_type=allure.attachment_type.TEXT)
        return DatabaseStep.executeQuery(query)

    @staticmethod
    def readSQLFile(name):
        sql_path = os.path.join(os.path.dirname(__file__), '..', 'consultas', name+'.sql')
        with open(sql_path, 'r', encoding='utf-8') as file:
            query = file.read()
        return query
