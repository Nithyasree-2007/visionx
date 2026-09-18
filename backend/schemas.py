from typing import Optional, List
from pydantic import BaseModel, Field

class VehicleBase(BaseModel):
    vehicle_id: str
    plate_number: str
    vehicle_type: str
    company: str
    driver_name: Optional[str] = None
    contact_number: Optional[str] = None
    authorization_status: str = "authorized"
    permit_start_date: str
    permit_expiry_date: str
    notes: Optional[str] = None

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(BaseModel):
    vehicle_id: Optional[str] = None
    plate_number: Optional[str] = None
    vehicle_type: Optional[str] = None
    company: Optional[str] = None
    driver_name: Optional[str] = None
    contact_number: Optional[str] = None
    authorization_status: Optional[str] = None
    permit_start_date: Optional[str] = None
    permit_expiry_date: Optional[str] = None
    notes: Optional[str] = None

class VehicleOut(VehicleBase):
    id: str

    class Config:
        from_attributes = True

class DetectionOut(BaseModel):
    id: str
    timestamp: str
    camera_id: str
    vehicle_id: Optional[str] = None
    vehicle_type: str
    plate_number: str
    ocr_confidence: float
    image_path: Optional[str] = None
    authorization_status: str
    plate_quality_score: float

    class Config:
        from_attributes = True

class AlertUpdate(BaseModel):
    status: str
    resolution_notes: Optional[str] = None

class AlertOut(BaseModel):
    id: str
    type: str
    plate_number: str
    timestamp: str
    camera_id: str
    camera_name: Optional[str] = None
    status: str
    title: str
    description: str
    resolution_notes: Optional[str] = None

    class Config:
        from_attributes = True

class EntryExitLogOut(BaseModel):
    id: str
    vehicle_id: str
    plate_number: str
    vehicle_type: str
    company: str
    driver_name: Optional[str] = None
    camera_id: str
    entry_time: str
    exit_time: Optional[str] = None
    duration_minutes: Optional[int] = None
    status: str
    authorization_status: str
    ocr_confidence: float
    date: str

    class Config:
        from_attributes = True

class HourlyTraffic(BaseModel):
    hour: str
    count: int

class VehicleTypeCount(BaseModel):
    name: str
    count: int
    percentage: int

class AverageStay(BaseModel):
    type: str
    duration_minutes: int

class FrequentlySeenVehicle(BaseModel):
    plate_number: str
    vehicle_type: str
    company: str
    visit_count: int
    authorization_status: str
    last_seen: str

class OCRPerformance(BaseModel):
    successful_ocr: int
    low_confidence_ocr: int
    unreadable_plates: int
    success_rate: float

class AnalyticsOut(BaseModel):
    total_vehicles_today: int
    active_vehicles_on_site: int
    authorized_vehicles: int
    unauthorized_vehicles: int
    total_plate_detections: int
    low_confidence_ocr_detections: int
    vehicles_per_hour: List[HourlyTraffic]
    vehicle_types: List[VehicleTypeCount]
    average_stay_by_type: List[AverageStay]
    frequently_seen_vehicles: List[FrequentlySeenVehicle]
    ocr_performance: OCRPerformance
