# This is a sample Python script.
from db.connection import get_db_connection
from db.querys import UserQueries


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('joselito')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def main():
    # Ejemplo de uso
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Obtener todos los usuarios
        query = UserQueries.get_all_users()
        cursor.execute(query)
        users = cursor.fetchall()
        print("Usuarios:", users)

if __name__ == "__main__":
    main()