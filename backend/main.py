from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Trip:
    id: Optional[int]= None
    name: str
    created_at=  field(default_factory=lambda: datetime.utcnow().isoformat())

@dataclass
class Party:
    name: str
    id: Optional[int] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
@dataclass
class Member:
        name: str
        email: str
        id: Optional[int]= None
        trip_id: Optional[int]= None
        party_id: Optional[int]= None

@dataclass
class Expense:
      amount: float
      paid_by: Optional[Member] = None
      trip_id: Optional[int]= None
      party_id: Optional[int]=None
      id: Optional[int]= None
      description: Optional[str]= None
      created_at= field(default_factory=lambda: datetime.utcnow().isoformat())
      
@dataclass
class Share:
      member: Member
      to_be_paid: float
      expense_id: Optional[int]= None
      id: Optional[int]= None



