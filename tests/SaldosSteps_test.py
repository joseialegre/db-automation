import allure
import pytest
from db.ProveedorStep import ProveedorStep


@allure.suite("Referencias entre Saldos y Cre_Saldos")
@allure.title("Se verifica la consistencia de referencias entre Saldos y Cre_Saldos")
@pytest.mark.saldos
def test_cre_saldos():
    rows = ProveedorStep.saldos_y_cresaldos()
    if len(rows) > 0:
        assert False, "¡Existen inconsistencias!"