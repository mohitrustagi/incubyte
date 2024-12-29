from fastapi.testclient import TestClient
from datetime import datetime
import pytest

from app.settings import Settings


@pytest.fixture(autouse=True, params=[True])
def mode(request) -> None:
    """
    Run all the tests in this file in both in_database and in_memory mode.
    """
    Settings.in_database = request.param


def test_create_appointment(client: TestClient):
    pass

def test_invalid_patient(client: TestClient):
    response = client.post('/doctor/appointments', json=(dict(patient_id='InvalidID', doctor_schedule_id='23', appointment_datetime='')))
    assert response.status_code == 422

def test_invalid_doctor(client: TestClient):
    response = client.post('/doctor/appointments', json=(dict(patient_id='0', doctor_id='invalidID', location='dummy location', appointment_datetime='2024-12-29T12:36:46.121')))
    assert response.status_code == 422

def test_invalid_location(client: TestClient):
    response = client.post('/doctor/appointments', json=(dict(patient_id='0', doctor_id='0', location='', appointment_datetime='2024-12-29T12:36:46.121Z')))
    assert response.status_code == 422

def test_duplicate_appointment(client: TestClient):
    response = client.post('/doctor/appointments', json=(dict(patient_id='0', doctor_id='0', location='Lucknow', appointment_datetime='2025-12-29T12:36:46.121')))
    assert response.status_code == 200
    response = client.post('/doctor/appointments', json=(dict(patient_id='0', doctor_id='0', location='Lucknow', appointment_datetime='2025-12-29T12:36:46.121')))
    assert response.status_code == 422

def test_invalid_appointment_time(client: TestClient):
    response = client.post('/doctor/appointments', json=(dict(patient_id='0', doctor_id='0', location='Lucknow', appointment_datetime='2023-12-29T12:36:46.121')))
    assert response.status_code == 422

def test_list_appointments(client: TestClient):
    client.post('/doctor/appointments', json=(dict(patient_id='0', doctor_id='0', location='location', appointment_datetime='2025-12-29T12:36:46.121')))
    response = client.get('/doctor/0/appointments')
    json_response = response.json()
    assert(len(json_response)) == 1

def cancel_user_appointment(client: TestClient):
    resp = client.post('/doctor/appointments', json=(dict(patient_id='0', doctor_id='0', location='location', appointment_datetime='2025-12-29T12:36:46.121')))
    assert resp.status_code == 200
    






