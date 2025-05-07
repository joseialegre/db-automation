import allure
import pytest
from db.ProveedorStep import ProveedorStep

@allure.parent_suite("Tarjetas")
@allure.suite("TJD_REL_TARJETA_CUENTA sin vínculo en TJD_ESTADO_TARJETA_CUENTA")
@allure.title("Se verifica la consistencia de referencias entre Saldos y Cre_Saldos")
@pytest.mark.tarjetas
def test_cre_saldos():
    rows = ProveedorStep.saldos_y_cresaldos()
    if len(rows) > 0:
        assert False, "Existen " + str(len(rows)) + " Tarjetas con estados no válidos"