from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field


# ==========================================
# VISIT SCHEMAS
# ==========================================

class VisitBase(BaseModel):
    visit_date: datetime = Field(..., description="Date and time of the visit")
    doctor_name: str = Field(..., min_length=1, max_length=100, description="Name of the attending doctor")
    diagnosis: str = Field(..., min_length=1, description="Medical diagnosis notes")
    prescription: Optional[str] = Field(None, description="Prescribed medications or instructions")


class VisitCreate(VisitBase):
    """Used when creating a new visit record via POST."""
    pass


class VisitUpdate(BaseModel):
    """Used when updating an existing visit record via PUT."""
    visit_date: Optional[datetime] = None
    doctor_name: Optional[str] = Field(None, min_length=1, max_length=100)
    diagnosis: Optional[str] = Field(None, min_length=1)
    prescription: Optional[str] = None


class VisitResponse(VisitBase):
    """Used when returning visit details back to the client."""
    id: int
    patient_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ==========================================
# PATIENT SCHEMAS
# ==========================================

class PatientBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Full name of the patient")
    age: int = Field(..., ge=0, le=130, description="Age in years")
    gender: str = Field(..., description="Gender (e.g. Male, Female, Other)")
    contact_number: str = Field(..., min_length=7, max_length=20, description="Primary contact phone number")
    address: Optional[str] = Field(None, max_length=255, description="Residential address")


class PatientCreate(PatientBase):
    """Used when registering a new patient via POST."""
    pass


class PatientUpdate(BaseModel):
    """Used when updating existing patient details via PUT."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    age: Optional[int] = Field(None, ge=0, le=130)
    gender: Optional[str] = None
    contact_number: Optional[str] = Field(None, min_length=7, max_length=20)
    address: Optional[str] = Field(None, max_length=255)


class PatientResponse(PatientBase):
    """Used for general patient list and basic info responses."""
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PatientDetailResponse(PatientResponse):
    """Used when fetching a single patient including all their visit history."""
    visits: List[VisitResponse] = []

    model_config = ConfigDict(from_attributes=True)

