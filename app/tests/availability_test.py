from fastapi.testclient import TestClient
from datetime import datetime
import pytest

from app.settings import Settings


@pytest.fixture(autouse=True, params=[True, False])
def mode(request) -> None:
    """
    Run all the tests in this file in both in_database and in_memory mode.
    """
    Settings.in_database = request.param


def test_create_appointment(client: TestClient):
    pass

def test_invalid_patient_when_create_appointment(client: TestClient):
    response = client.post('/doctor/availability', json=(dict(patient_id='InvalidID', doctor_schedule_id='23', appointment_datetime='')))
    assert response.status_code == 422
