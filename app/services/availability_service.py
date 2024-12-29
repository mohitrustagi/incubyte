from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from app.database.db import DB
from app.models import DoctorAppointment
from app.models.error import UnprocessableEntity
from fastapi import HTTPException



class AvailabilityService:
    def __init__(self, db: DB):
        self.db = DB

    def add_appointments(self, patient_id: int, doctor_id: int, location: str, appointment_datetime: datetime) -> int:
        dict_result = self.db.execute(f"select * from patients where id = {patient_id}")
        if not dict_result:
            raise HTTPException(status_code=422, detail='Patient not found!')

        doctor_result = self.db.execute(f"select * from doctors where id = {doctor_id}")
        if not doctor_result:
            raise HTTPException(status_code=422, detail='Doctor not found!')

        if not location:
            raise HTTPException(status_code=422, detail='Location not found!')

        if appointment_datetime <= datetime.now():
            raise HTTPException(status_code=422, detail='Appointment time cannot be in the past!')
        
        str_appointment_datetime = appointment_datetime.strftime('%Y-%m-%d %H:%M:00')
        duplicate_appointment = self.db.execute(f"select * from doctor_appointments where doctor_id={doctor_id} and location='{location}' and appointment_datetime='{str_appointment_datetime}'")
        if duplicate_appointment:
            raise HTTPException(status_code=422, detail='Duplicate appointment time!')

        resp = self.db.execute(f"INSERT INTO doctor_appointments (patient_id, doctor_id, location, appointment_datetime) VALUES ({patient_id}, {doctor_id}, '{location}', '{str_appointment_datetime}')")
        return self.db.last_row_id

    
    def list_appointments(self, doctor_id: int):
        dict_result = self.db.execute(
            'SELECT * '
            f'FROM doctor_appointments where doctor_id={doctor_id}'
        )
        return [
            DoctorAppointment(**res) for res in dict_result
        ]

