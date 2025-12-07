from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict, Tuple

@dataclass
class Trip:
     name: str
     id: Optional[int]= None
     created_at :str=  datetime.utcnow().isoformat()

    
@dataclass
class Member:
        name: str
        email: str
        id: Optional[int]= None
        trip_id: Optional[int]= None

@dataclass
class Expense:
      amount: float
      paid_by: Optional[Member] = None
      trip_id: Optional[int]= None
      id: Optional[int]= None
      description: Optional[str]= None
      created_at: str= datetime.utcnow().isoformat()
      
@dataclass
class Share:
      member: Member
      to_be_paid: float
      expense_id: Optional[int]= None
      id: Optional[int]= None


class ExpenseManager:
      
      def __init__(self):
            self.trips: Dict[int,Trip]= {}
            self.members: Dict[int,Member]= {}
            self.expenses: Dict[int,Expense]= {}
            self.shares: Dict[int,Share]= {}

            self.trip_counter=1
            self.member_counter=1
            self.expense_counter=1
            self.share_counter=1

      def create_trip(self, name:str) -> Trip:
            trip= Trip(name=name, id=self.trip_counter)
            self.trips[self.trip_counter]= name
            self.trip_counter += 1
            return trip

      def get_trip(self, trip_id:int) -> Optional[Trip]:
            return self.trips.get(trip_id)
      
      def list_trips(self) -> List[Trip]:
            return list(self.trips.values())
      
      def add_member(self, name:str, email:str, trip_id: int)-> Member:
            member= Member(name=name, email=email, id=self.member_counter, trip_id=trip_id)
            self.members[self.member_counter]= member
            self.member_counter += 1
            return member
      
      def list_members(self, trip_id:int) -> List[Member]:
            return [member for member in self.members.values() if member.trip_id == trip_id]          
      
      def add_expense_equal_split(self, amount:float, paid_by:Member, trip_id:int, description:Optional[str]=None) -> Tuple[Expense, List[Share]]:
            
            members= self.list_members(trip_id)
            if not members:
                  raise ValueError("No members found in the trip to split the expense.")
            
            expense = Expense(amount=round(amount,2), paid_by=paid_by, trip_id=trip_id, description=description, id=self.expense_counter)
            self.expenses[self.expense_counter]= expense
            self.expense_counter += 1

            split_amount= round(amount,2) / len(members)
            per_head= round(split_amount,2)

            shares= []
            for member in members:
                  share= Share(member=member, to_be_paid=per_head, expense_id=expense.id, id=self.share_counter)
                  self.shares[self.share_counter]= share
                  self.share_counter += 1
                  shares.append(share)
            
            return expense, shares
      
      def list_expenses(self, trip_id:int) -> List[Expense]:
            return [expense for expense in self.expenses.values() if expense.trip_id == trip_id]
      
      def list_shares(self, expense_id:int) -> List[Share]:
            return [share for share in self.shares.values() if share.expense_id == expense_id]
      
      