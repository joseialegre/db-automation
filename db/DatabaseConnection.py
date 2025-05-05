import allure
from sqlalchemy import create_engine
import os

class DatabaseConnection:
    def __init__(self):
        self.server = os.getenv("DB_SERVER", "topaz-tesoreria-db.nbch.com.ar")
        self.database = os.getenv("DB_NAME", "tesoreria")
        self.username = os.getenv("DB_USER", "aut_apit")
        self.password = os.getenv("DB_PASSWORD", "regreso584")
        self.connection_url = (
            f"mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}"
            "?driver=ODBC+Driver+13+for+SQL+Server"
        )
        self.engine = None

    def __enter__(self):
        self.engine = create_engine(self.connection_url)
        return self.engine.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.engine:
            self.engine.dispose()

def get_db_connection():
    return DatabaseConnection()