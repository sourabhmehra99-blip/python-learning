# Create a class called PersonAccount. 
# It has firstname, lastname, incomes, expenses properties 
# and it has total_income, total_expense, account_info, add_income, add_expense 
# and account_balance methods. Incomes is a set of incomes and its description. 
# The same goes for expenses.

class PersonAccount:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenes = {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expence(self):
        return sum (self.expenes.values())

    def account_info(self):
        return f"Account holder: {self.firstname} {self.lastname}\nTotal Expence: {self.total_expence}\nTotal Income: {self.total_expence}"


p1 = PersonAccount("sourabh","mehta")

p1.total_income("job",10000)
p1.total_income("freelancing",5000)

p1.total_expence("rent",2000)
p1.total_expence("food",1000)
print(p1.account_info())