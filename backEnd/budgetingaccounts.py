import json

class BudgetAccount:
    def __init__(self, balance=0, food_budget=0, entertainment_budget=0, savings_budget=0):
        self.balance = balance
        self.food_budget = food_budget
        self.entertainment_budget = entertainment_budget
        self.savings_budget = savings_budget
        try:
            with open("C:/Users/William/Documents/GitHub/QHacks/backEnd/USER DATA OUT.json", "r") as file:
                data = json.load(file)
                self.balance = data["balance"]
                self.food_budget = data["food_budget"]
                self.entertainment_budget = data["entertainment_budget"]
                self.savings_budget = data["savings_budget"]
        except:
            self.balance = 0
            self.food_budget = 0
            self.entertainment_budget = 0
            self.savings_budget = 0

    def check_balance(self):
        return self.balance

    def track_expense(self, category, amount):
        if category == "food":
            if self.balance - amount >= 0:
                self.balance -= amount
                return "Expense recorded"
            else:
                return "Insufficient funds"
        else:
            return "Invalid category"

my_budget = BudgetAccount()
print(my_budget.check_balance())
print(my_budget.track_expense("food", 200))

with open("C:/Users/William/Documents/GitHub/QHacks/backEnd/USER DATA OUT.json", "w") as file:
    json.dump({"balance": my_budget.balance, "food_budget": my_budget.food_budget, "entertainment_budget": my_budget.entertainment_budget, "savings_budget": my_budget.savings_budget}, file)

print("balance:", my_budget.balance)
print("Recommended food budget:", my_budget.food_budget)
print("Recommended entertainment budget:", my_budget.entertainment_budget)
print("Recommended savings budget:", my_budget.savings_budget)
