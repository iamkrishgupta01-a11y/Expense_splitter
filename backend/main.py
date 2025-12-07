from core.manager import Trip, Party, Member, Expense, Share 
from core.manager import Manager

mgr = Manager()
t = mgr.create_trip("Goa Trip")
m1 = mgr.add_member_to_trip(t.id, "Rahul", "rahul@example.com")
m2 = mgr.add_member_to_trip(t.id, "Priya", "priya@example.com")
m3 = mgr.add_member_to_trip(t.id, "Arman", "arman@example.com")

exp = mgr.add_expense_to_trip_equal_split(t.id, 600, "Dinner")
print("Expense id:", exp.id, "amount:", exp.amount)
shares = mgr.get_shares_for_expense(exp.id)
for s in shares:
    print(s.member.email, "owes", s.to_be_paid)

print("Balances:", mgr.compute_balances_for_trip(t.id))



