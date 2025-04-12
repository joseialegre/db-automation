class UserQueries:
    @staticmethod
    def get_all_users():
        return "SELECT * FROM Persona"

    @staticmethod
    def get_user_by_id(user_id):
        return "SELECT * FROM Cliente WHERE id = ?", (user_id,)

# Puedes añadir más clases para diferentes entidades/tablas
class ProductQueries:
    @staticmethod
    def get_products_by_category(category_id):
        return "SELECT * FROM Cliente WHERE categoria_id = ?", (category_id,)