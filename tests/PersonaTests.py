from db.connection import get_db_connection  # Ajusta la importación según tu estructura


def test_query_personas_trae_datos():
    # Ejecuta la query directamente (como en tu código original)
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM persona")  # Usa tu query real aquí
        personas = cursor.fetchall()
    # Validación: Falla si no hay datos
    assert len(personas) > 0, "¡La query no devolvió ningún registro!"

def test_se_busca_persona_especifica():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PERSONA WHERE CUIT = 1")
        personas = cursor.fetchall()
    assert len(personas) > 0, "La query no trajo na..."
