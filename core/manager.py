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
                  raise ValueError("No members found in the given trip to split the expense.")
            


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
      
      
      def get_balance(self, member_id:int) -> float:
           total_owed= sum(share.to_be_paid for share in self.shares.values() if share.member.id == member_id)
             
           
      #CLI now 


      
def main():
      manager = ExpenseManager()
       
      while True:
            print("Please Enter the corresponding value for your operation")
            print("1. Create Trip")
            print("2. Add Member to Trip")            
            print("3. Add Expense with Equal Split")
            print("4. List Trips")                                      
            print("5. List Members in a Trip")
            print("6. List Expenses in a Trip")
            print("7. List Shares for an Expense")
            print("8. Get Member Balance")
            print("0. Exit")
      
            
            choice = input("Enter your choice: ").strip()

            
            if choice == "1":
             name = input("Enter trip name: ").strip()
             trip = manager.create_trip(name)
             print(f"Trip created: {trip}")

            
            elif choice == "2":
             trip_id = int(input("Enter trip ID: ").strip())
             name = input("Enter member name: ").strip()
             email = input("Enter member email: ").strip()          #I have used this for e mail integration later.(will do it with some more features)
             member = manager.add_member(name, email, trip_id)
             print(f"Member added iwth the following info: {member}")     

            
            
            
            elif choice == "3":
             trip_id = int(input("Enter trip ID: ").strip())
             amount = float(input("Enter expense amount: ").strip())
             paid_by_id = int(input("Enter member ID who paid: ").strip())
             description = input("Enter expense description (optional): ").strip() or None
             paid_by = manager.members.get(paid_by_id)
             if not paid_by:
                  print("Invalid member ID.")
                  continue
             
             expense, shares = manager.add_expense_equal_split(amount, paid_by, trip_id, description)
             print(f"Expense added: {expense}")
             print("Shares:")
             for share in shares:
                  print(share)      


           
           

            
            
            elif choice == "4":
             trips = manager.list_trips()
             print("Trips:")
             for trip in trips:
                  print(trip)       

            


            
            elif choice == "5":
             trip_id = int(input("Enter trip ID: ").strip())
             members = manager.list_members(trip_id)
             print("Members:")
             for member in members:
                  print(member)

           
           
            elif choice == "6":
             trip_id = int(input("Enter trip ID: ").strip())
             expenses = manager.list_expenses(trip_id)
             print("Expenses:")
             for expense in expenses:
                  print(expense)    

            



            
            elif choice == "7":
             expense_id = int(input("Enter expense ID: ").strip())
             shares = manager.list_shares(expense_id)
             print("Shares:")
             for share in shares:
                  print(share)
            
            
            elif choice == "0":
             print("Exiting...........")
             break       
            

            elif choice == 8:
                 member_id = int(input("Enter member ID: ").strip())
                 balance = manager.get_balance(member_id)
                 print(f"Balance for the member is : {balance}")
           
           
            else:
             print("Invalid choice. Please try again.")      

if __name__ == "__main__":
      main()


