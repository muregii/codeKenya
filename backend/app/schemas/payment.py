from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field, field_validator


class CustomerDetails(BaseModel):
    email: Optional[str] = Field(None, example="customer@example.com")
    phone_number: Optional[str] = Field(None, example="254712345678")
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")

class PaymentCreate(BaseModel):
    amount: float = Field(..., gt=0, example=1000.00)
    currency: str = Field("KES", example="KES")
    narrative: str = Field("Payment for services", example="Order #12345")
    payment_method: str = Field("MPESA", example="MPESA")
    redirect_url: Optional[str] = Field(None, example="https://codekenya.org/")
    customer: Optional[CustomerDetails] = None
    payment_metadata: Optional[Dict[str, Any]] = Field(None, example={"order_id": "12345"})

    @field_validator('payment_method')
    def validate_payment_method(cls, v):
        valid_methods = ["MPESA", "CARD", "BANK"]
        if v.upper() not in valid_methods:
            raise ValueError(f"Invalid payment method. Must be one of {valid_methods}")
        return v.upper()

class PaymentResponse(BaseModel):
    invoice_id: str
    payment_url: Optional[str]
    status: str
    amount: float
    currency: str
    payment_method: str
    created_at: datetime