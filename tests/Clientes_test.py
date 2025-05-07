import allure
import pytest
from db.ProveedorStep import ProveedorStep


@allure.parent_suite("Clientes")
@allure.suite("Clientes sin vínculo a sucursal")
@allure.title("Se verifican los clientes vinculados a sucursales")
@pytest.mark.clientes
def test_clientes_sucursal():
    rows = ProveedorStep.buscar_clientes_sucursal()
    if len(rows) > 0:
        assert False, "Existen "+str(len(rows))+" Clientes con Sucursal inexistente"

@allure.parent_suite("Clientes")
@allure.suite("Clientes sin vínculo a persona física o jurídica")
@allure.title("Se verifican los clientes vinculados a personas")
@pytest.mark.clientes
def test_clientes_persona():
    rows = ProveedorStep.buscar_clientes_persona()
    if len(rows) > 0:
        assert False, "Existen "+str(len(rows))+" Clientes Vinculados a persona no válidas"