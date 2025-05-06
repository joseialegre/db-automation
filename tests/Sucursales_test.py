import allure
import pytest
from db.ProveedorStep import ProveedorStep

@allure.parent_suite("Sucursales")
@allure.suite("Saldo sin vínculo a Sucursal")
@allure.title("Se verifica la consistencia de referencias entre Sucursales y Saldos")
@pytest.mark.sucursales
def test_sucursales_saldos():
    rows = ProveedorStep.sucursales_saldos()
    if len(rows) > 0:
        assert False, "¡Existen inconsistencias!"
