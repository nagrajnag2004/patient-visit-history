from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(
    tags=["Visits"]
)


# Helper function to check if patient exists
def get_patient_or_404(patient_id: int, db: Session):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} does not exist. Cannot perform visit operations."
        )
    return patient


# 1. Add a new visit for an existing patient
@router.post(
    "/patients/{patient_id}/visits",
    response_model=schemas.VisitResponse,
    status_code=status.HTTP_201_CREATED
)
def create_visit_for_patient(
    patient_id: int,
    visit_in: schemas.VisitCreate,
    db: Session = Depends(get_db)
):
    """
    Record a new medical visit for a registered patient.
    Checks that the patient exists first, then persists the visit.
    """
    # Ensure the parent patient exists
    get_patient_or_404(patient_id, db)

    new_visit = models.Visit(
        patient_id=patient_id,
        visit_date=visit_in.visit_date,
        doctor_name=visit_in.doctor_name,
        diagnosis=visit_in.diagnosis,
        prescription=visit_in.prescription
    )
    db.add(new_visit)
    db.commit()
    db.refresh(new_visit)
    return new_visit


# 2. Retrieve all visits of a particular patient
@router.get(
    "/patients/{patient_id}/visits",
    response_model=List[schemas.VisitResponse]
)
def get_patient_visits(patient_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all historical visit records for a specific patient.
    """
    # Ensure patient exists
    get_patient_or_404(patient_id, db)

    visits = (
        db.query(models.Visit)
        .filter(models.Visit.patient_id == patient_id)
        .order_by(models.Visit.visit_date.desc())
        .all()
    )
    return visits


# 3. Retrieve individual visit details
@router.get(
    "/visits/{visit_id}",
    response_model=schemas.VisitResponse
)
def get_visit_by_id(visit_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of a single visit record using its unique Visit ID.
    """
    visit = db.query(models.Visit).filter(models.Visit.id == visit_id).first()
    if not visit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Visit with ID {visit_id} not found."
        )
    return visit


# 4. Update visit information
@router.put(
    "/visits/{visit_id}",
    response_model=schemas.VisitResponse
)
def update_visit(
    visit_id: int,
    visit_update: schemas.VisitUpdate,
    db: Session = Depends(get_db)
):
    """
    Update diagnosis, doctor name, prescription, or date of an existing visit record.
    """
    visit = db.query(models.Visit).filter(models.Visit.id == visit_id).first()
    if not visit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Visit with ID {visit_id} not found."
        )

    update_data = visit_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(visit, field, value)

    db.commit()
    db.refresh(visit)
    return visit


# 5. Delete a visit record
@router.delete(
    "/visits/{visit_id}",
    status_code=status.HTTP_200_OK
)
def delete_visit(visit_id: int, db: Session = Depends(get_db)):
    """
    Delete a single visit record by ID.
    """
    visit = db.query(models.Visit).filter(models.Visit.id == visit_id).first()
    if not visit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Visit with ID {visit_id} not found."
        )

    db.delete(visit)
    db.commit()
    return {"message": f"Visit with ID {visit_id} has been successfully deleted."}

