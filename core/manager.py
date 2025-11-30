from dataclasses import dataclass, field, replace
from datetime import datetime
from typing import Optional, List, Dict, Tuple

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

class Manager:
      

      def __init__(self):
            self.trip_seq =0
            self.party_seq =0
            self.member_seq =0
            self.expense_seq =0
            self.share_seq =0

            self.trips = Dict[int, Trip]={}
            self.parties = Dict[int, Party]={}
            self.members = Dict[int, Member]={}
            self.expenses = Dict[int, Expense]={}
            self.shares = Dict[int, Share]={}


            def create_trip(self, name: str) :
                  self.trip_seq +=1
                  t= Trip(name = name, id= self.trip_seq)
                  self.trips[t.id]= t
                  return t
           
            def create_party(self, name: str) :
                    self.party_seq +=1
                    p= Party(name = name, id= self.party_seq)
                    self.parties[p.id]= p
                    return p
            
            def get_trip(self, trip_id: int) :
             return self.trips.get(trip_id)

            def get_party(self, party_id: int) :
             return self.parties.get(party_id)

            def list_trips(self):
             return list(self.trips.values())

            def list_parties(self):
             return list(self.parties.values())
            
            def add_member_to_trip(self, name :str, email:str, trip_id:int):
                if trip_id not in self.trips:
                    raise ValueError("Any such Trip does not exist")
                email_norm = email.strip().lower()
                for m in self.members.values():
                    if m.email.strip().lower() == email_norm and m.trip_id == trip_id:
                        return m
                self.member_seq+=1
                m= Member(name=name, email=email, trip_id=trip_id, id=self.member_seq)
                self.members[m.id]= m       
                return m

            def add_member_to_party(self, name :str, email:str, party_id:int):
                if party_id not in self.parties:
                    raise ValueError("Any such Party does not exist")
                email_norm = email.strip().lower()
                for m in self.members.values():
                    if m.email.strip().lower() == email_norm and m.party_id == party_id:
                        return m
                self.member_seq+=1
                m= Member(name=name, email=email, party_id=party_id, id=self.member_seq)
                self.members[m.id]= m       
                return m