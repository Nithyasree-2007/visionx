from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from .database import Base

class VehicleModel(Base):
    __tablename__ = "vehicles"

    id = Column(String(50), primary_key=True, index=True)
    vehicle_id = Column(String(50), unique=True, index=True, nullable=False)
    plate_number = Column(String(30), unique=True, index=True, nullable=False)
    vehicle_type = Column(String(50), nullable=False)  # Truck, Concrete Mixer, etc.
    company = Column(String(100), nullable=False)
    driver_name = Column(String(100), nullable=True)
    contact_number = Column(String(30), nullable=True)
    authorization_status = Column(String(20), default="authorized", nullable=False)  # authorized, unauthorized, expired
    permit_start_date = Column(String(30), nullable=False)
    permit_expiry_date = Column(String(30), nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class DetectionModel(Base):
    __tablename__ = "detections"

    id = Column(String(50), primary_key=True, index=True)
    timestamp = Column(String(50), nullable=False)
    camera_id = Column(String(50), nullable=False, index=True)
    vehicle_id = Column(String(50), nullable=True)
    vehicle_type = Column(String(50), nullable=False)
    plate_number = Column(String(30), nullable=False, index=True)
    ocr_confidence = Column(Float, nullable=False)
    image_path = Column(String(255), nullable=True)
    authorization_status = Column(String(20), nullable=False)
    plate_quality_score = Column(Float, default=80.0)
    created_at = Column(DateTime, default=datetime.utcnow)

class AlertModel(Base):
    __tablename__ = "alerts"

    id = Column(String(50), primary_key=True, index=True)
    type = Column(String(50), nullable=False)  # unauthorized_vehicle, expired_permit, low_confidence_ocr, unreadable_plate
    plate_number = Column(String(30), nullable=False, index=True)
    timestamp = Column(String(50), nullable=False)
    camera_id = Column(String(50), nullable=False)
    camera_name = Column(String(100), nullable=True)
    status = Column(String(20), default="new", nullable=False)  # new, reviewed, resolved
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    resolution_notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class EntryExitLogModel(Base):
    __tablename__ = "entry_exit_logs"

    id = Column(String(50), primary_key=True, index=True)
    vehicle_id = Column(String(50), nullable=False)
    plate_number = Column(String(30), nullable=False, index=True)
    vehicle_type = Column(String(50), nullable=False)
    company = Column(String(100), nullable=False)
    driver_name = Column(String(100), nullable=True)
    camera_id = Column(String(50), nullable=False)
    entry_time = Column(String(50), nullable=False)
    exit_time = Column(String(50), nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    status = Column(String(30), default="Inside Perimeter")
    authorization_status = Column(String(20), nullable=False)
    ocr_confidence = Column(Float, default=95.0)
    date = Column(String(20), nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
