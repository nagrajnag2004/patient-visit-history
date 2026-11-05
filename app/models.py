from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    contact_number = Column(String(20), nullable=False)
    address = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # One-to-Many Relationship: One Patient has many Visits.
    # cascade="all, delete-orphan" ensures when a patient is deleted, their visits are also deleted.
    visits = relationship(
        "Visit",
        back_populates="patient",
        cascade="all, delete-orphan",
        passive_deletes=True
    )


class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    patient_id = Column(
        Integer,
        ForeignKey("patients.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    visit_date = Column(DateTime, nullable=False)
    doctor_name = Column(String(100), nullable=False)
    diagnosis = Column(Text, nullable=False)
    prescription = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Back reference to the parent Patient
    patient = relationship("Patient", back_populates="visits")

