from pydantic import BaseModel
from datetime import datetime, time
from enum import Enum


class Patient(BaseModel):
    id: int
    name: str


class Doctor(BaseModel):
    id: int
    first_name: str
    last_name: str


class Location(BaseModel):
    id: int
    address: str


class DoctorLocation(BaseModel):
    """
    This indicates that a doctor works at a location. Locations can have
    multiple doctors, and doctors can have multiple locations
    """
    id: int
    doctor_id: int
    location_id: int


class DayOfWeek(str, Enum):
    SUNDAY = 'Sunday' 
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'


class DoctorSchedule(BaseModel):
    """
    This represents the doctor's availability time slot for the day of the week.
    """
    id: int
    doctor_id: int
    location_id: int
    day_of_the_week: DayOfWeek
    start_time: time
    end_time: time


class DoctorAppointment(BaseModel):
    """
    This represents a patient's appointment to see a doctor.
    """
    id: int
    patient_id: int
    doctor_id: int
    location: str
    appointment_datetime: datetime
    status: str  

