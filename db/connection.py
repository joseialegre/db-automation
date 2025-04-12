import pyodbc
import os

class DatabaseConnection:
    def __init__(self):
        self.server = os.getenv("DB_SERVER", "localhost,1433")
        self.database = os.getenv("DB_NAME", "master")
        self.username = os.getenv("DB_USER", "jose")
        self.password = os.getenv("DB_PASSWORD", "apple951")
        self.connection = None

    def __enter__(self):
        self.connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'UID={self.username};'
            f'PWD={self.password}'
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

def get_db_connection():
    return DatabaseConnection()