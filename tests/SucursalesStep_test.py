import allure
import pytest
from db.querys import UserQueries


@allure.suite("Referencias entre Sucursales y Saldos")
@allure.title("Se verifica la consistencia de referencias entre Sucursales y Saldos")
@pytest.mark.sucursales
def test_sucursales_saldos():
    rows = UserQueries.sucursales_saldos()
    if len(rows) > 0:
        assert False, "¡Existen inconsistencias!"
