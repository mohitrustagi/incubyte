from datetime import datetime
from pydantic import BaseModel

class AddAppointmentRequest(BaseModel):
    patient_id: int
    doctor_schedule_id: int
    appointment_datetime: datetime
