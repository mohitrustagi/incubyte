from datetime import datetime
from pydantic import BaseModel

class AddAppointmentRequest(BaseModel):
    patient_id: int
    doctor_id: int
    location: str
    appointment_datetime: datetime
