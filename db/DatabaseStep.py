import allure
import pandas as pd
import io

from db.DatabaseConnection import get_db_connection

class DatabaseStep:

    @staticmethod
    @allure.step("Se ejecuta la consulta en la base de datos de Topaz")
    def executeQuery(query):
        with get_db_connection() as conn:
            dataframe = pd.read_sql_query(query, conn)
            DatabaseStep.validate(dataframe, query)
            return dataframe

    @staticmethod
    @allure.step("Se obtiene respuesta con resultado")
    def validate(dataframe, query):
        allure.attach(query, name="Consulta SQL:", attachment_type=allure.attachment_type.TEXT)
        csv_buffer = io.StringIO()
        dataframe.to_csv(csv_buffer, index=False)
        allure.attach(
            csv_buffer.getvalue(),
            name="Respuesta:",
            attachment_type=allure.attachment_type.CSV
        )
