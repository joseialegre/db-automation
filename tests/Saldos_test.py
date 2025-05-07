import allure
import pytest
from db.ProveedorStep import ProveedorStep

@allure.parent_suite("Saldos")
@allure.suite("Cre_Saldos sin vínculo en Saldos")
@allure.title("Se verifica la consistencia de referencias entre Saldos y Cre_Saldos")
@pytest.mark.saldos
def test_cre_saldos():
    rows = ProveedorStep.saldos_y_cresaldos()
    if len(rows) > 0:
        assert False, "Existen " + str(len(rows)) + " Cre_Saldos sin referencia a Saldos"

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

@allure.parent_suite("Saldos")
@allure.suite("Vta_Saldos sin vínculo en Saldos")
@allure.title("Se verifica la consistencia de referencias entre Saldos y Vta_Saldos")
@pytest.mark.saldos
def test_vta_saldos():
    rows = ProveedorStep.saldos_y_vtasaldos()
    if len(rows) > 0:
        assert False, "Existen " + str(len(rows)) + " Vta_Saldos sin referencia a Saldos"

@allure.parent_suite("Saldos")
@allure.suite("MovimientosContables sin vínculo en Saldos")
@allure.title("Se verifica la consistencia de referencias entre Movimientos Contables y Saldos")
@pytest.mark.saldos
def test_movimientos_contables_saldos():
    rows = ProveedorStep.buscar_movimiento_contable_sin_saldo()
    if len(rows) > 0:
        assert False, "Existen " + str(len(rows)) + " Movimientos Contables sin referencia en Saldos"

@allure.parent_suite("Saldos")
@allure.suite("Grl Estados de Cuenta sin vínculo en Saldos")
@allure.title("Se verifica la consistencia de referencias entre Grl Estados de Cuenta y Saldos")
@pytest.mark.saldos
def test_grl_estado_cuenta_saldos():
    rows = ProveedorStep.buscar_estados_cuenta_sin_saldo()
    if len(rows) > 0:
        assert False, "Existen " + str(len(rows)) + " Movimientos Contables sin referencia en Saldos"
