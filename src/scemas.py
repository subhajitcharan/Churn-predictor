from pydantic import BaseModel,Field
from typing import Literal
class data(BaseModel):
    CreditScore: int = Field(..., ge=300, le=900)
    Age: int = Field(..., ge=18, le=100)
    Tenure: int = Field(..., ge=0, le=10)
    Balance: float = Field(..., ge=0)
    NumOfProducts: int = Field(..., ge=1, le=4)
    EstimatedSalary: float = Field(..., ge=0)
    Gender: Literal["Male", "Female"]
    HasCrCard: Literal["Yes", "No"]
    IsActiveMember: Literal["Yes", "No"]
    Geography:Literal["France","Germany","Spain"]
    class Config:
        json_schema_extra = {
            "example": {
                "CreditScore": 650,
                "Age": 40,
                "Tenure": 5,
                "Balance": 125000.0,
                "NumOfProducts": 2,
                "EstimatedSalary": 85000.0,
                "Gender": "Male",
                "HasCrCard": "Yes",
                "IsActiveMember": "Yes",
                "Geography": "Germany"
            }
            

            
        }