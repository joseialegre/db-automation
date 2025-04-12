import pyodbc
import os

class DatabaseConnection:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = pyodbc.connect(
            #f'DRIVER={{SQL Server Native Client 11.0}};'
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

# Configuración (puedes mover esto a un archivo de configuración)
def get_db_connection():
    return DatabaseConnection(
        server=os.getenv("DB_SERVER", "localhost,1433"),
        database=os.getenv("DB_NAME", "master"),
        username=os.getenv("DB_USER", "jose"),
        password=os.getenv("DB_PASSWORD", "apple951")
    )
