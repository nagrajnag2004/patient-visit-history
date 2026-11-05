from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


# 1. Register a new patient
@router.post("/", response_model=schemas.PatientResponse, status_code=status.HTTP_201_CREATED)
def create_patient(patient_in: schemas.PatientCreate, db: Session = Depends(get_db)):
    """
    Register a new patient into the system.
    Returns HTTP 201 Created with the saved patient data and generated ID.
    """
    new_patient = models.Patient(
        name=patient_in.name,
        age=patient_in.age,
        gender=patient_in.gender,
        contact_number=patient_in.contact_number,
        address=patient_in.address
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient


# 2. Retrieve all patients
@router.get("/", response_model=List[schemas.PatientResponse])
def get_all_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all registered patients with pagination support.
    """
    patients = db.query(models.Patient).offset(skip).limit(limit).all()
    return patients


# 3. Retrieve patient details by Patient ID
@router.get("/{patient_id}", response_model=schemas.PatientDetailResponse)
def get_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    """
    Retrieve full details of a specific patient including their medical visit history.
    """
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found."
        )
    return patient


# 4. Update patient information
@router.put("/{patient_id}", response_model=schemas.PatientResponse)
def update_patient(patient_id: int, patient_update: schemas.PatientUpdate, db: Session = Depends(get_db)):
    """
    Update details of an existing patient.
    Only updates the fields provided in the request body.
    """
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found."
        )

    # Convert update data into dict excluding unset fields
    update_data = patient_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(patient, field, value)

    db.commit()
    db.refresh(patient)
    return patient


# 5. Delete a patient record
@router.delete("/{patient_id}", status_code=status.HTTP_200_OK)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    """
    Delete a patient record by ID.
    Thanks to ON DELETE CASCADE, all associated visits will also be safely removed.
    """
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found."
        )

    db.delete(patient)
    db.commit()
    return {"message": f"Patient with ID {patient_id} and all related visits have been successfully deleted."}

