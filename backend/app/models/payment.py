from datetime import datetime

from sqlalchemy import JSON, Column, DateTime, Float, String

from ..db.database import Base


class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(String, primary_key=True, index=True)
    invoice_id = Column(String, unique=True, index=True)
    amount = Column(Float, nullable=False, default=8.0)
    currency = Column(String, default="KES")
    payment_method = Column(String, nullable=True)
    status = Column(String, nullable=True)
    customer_email = Column(String, nullable=True)
    customer_phone = Column(String, nullable=True)
    payment_metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)