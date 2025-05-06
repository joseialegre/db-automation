import allure
import pytest
from db.ProveedorStep import ProveedorStep

@allure.parent_suite("Saldos")
@allure.suite("Cre_Saldos sin vínculo a Saldos")
@allure.title("Se verifica la consistencia de referencias entre Saldos y Cre_Saldos")
@pytest.mark.saldos
def test_cre_saldos():
    rows = ProveedorStep.saldos_y_cresaldos()
    if len(rows) > 0:
        assert False, "¡Existen inconsistencias!"

@allure.parent_suite("Saldos")
@allure.suite("Saldos Inconsistentes")
@allure.title("Se verifica la consistencia de Saldos")
@pytest.mark.saldos
def test_saldos_inconsistentes():
    rows = ProveedorStep.buscar_saldos_inconsistentes()
    if len(rows) > 0:
        assert False, "Existen "+str(len(rows))+" saldos inconsistentes"

@allure.parent_suite("Saldos")
@allure.suite("CBUs Duplicados")
@allure.title("Se verifica la existencia de CBUs duplicados")
@pytest.mark.saldos
def test_cbu_duplicados():
    rows = ProveedorStep.buscar_cbus_duplicados()
    if len(rows) > 0:
        assert False, "Existen "+str(len(rows))+" CBUs Duplicados"
