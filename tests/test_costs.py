from fastapi.testclient import TestClient
from finops.main import app

client = TestClient(app)


def test_totals_and_budget():
    payload = client.post("/costs", json={"lines": [{'service': 'compute', 'cost': 70}, {'service': 'network', 'cost': 8}], "budget": 77.0}).json()
    assert payload["total"] == 78.0
    assert payload["over_budget"] is True
    assert payload["applied"] is False
