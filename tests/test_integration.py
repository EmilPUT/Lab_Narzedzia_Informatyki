import json
from src.models import Apartment
from src.manager import Manager
from src.models import Parameters
from pathlib import Path

def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key

def test_tenants_integration():
    parameters = Parameters()
    manager = Manager(parameters)

    with open("data/tenants.json", "r", encoding="utf-8") as f:
        expected_tenants = json.load(f)

    for tenant_id, tenant_data in expected_tenants.items():
        assert tenant_id in manager.tenants, f"Najemca {tenant_id} nie został znaleziony w managerze"
        
        tenant_obj = manager.tenants[tenant_id]
        expected_name = tenant_data["name"]
        
        assert tenant_obj.name == expected_name