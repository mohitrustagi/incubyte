from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from app.database.db import DB
# from app.models import Doctor, Location, DoctorLocation
from app.models.error import UnprocessableEntity



class AvailabilityService:
    """
    This is left up to you to implement, generally following the patterns in the repo.

    That said, *don't* feel obliged to make an abstract base class/interface for your chosen approach - you
    can simply write the service using either the database or in-memory approach from the beginning.
    We used that pattern for the doctor_service to have examples for both modes.
    """
    def __init__(self, db: DB):
        self.db = DB

    def add_appointment(self, patient_id: int, doctor_schedule_id: int, appointment_datetime: datetime) -> int:
        dict_result = self.db.execute(f"select * from patients where id = {patient_id}")
        if not dict_result:
            print("hello worldsddddd")
            raise UnprocessableEntity('Patient not found!')


        
