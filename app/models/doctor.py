from pydantic import BaseModel
from datetime import time
from enum import Enum


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


class DayOfWeek(int, Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class DoctorSchedule(BaseModel):
    """
    This represents the doctor's availability time slot for the day of the week.
    """
    id: int
    doctor_id: int
    day_of_the_week: DayOfWeek
    start_time: time
    end_time: time