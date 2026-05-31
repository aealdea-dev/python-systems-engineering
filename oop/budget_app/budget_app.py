class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    spent_amounts = [sum(-item['amount'] for item in cat.ledger if item['amount'] < 0) for cat in categories]
    total_spent = sum(spent_amounts)
    percentages = [int((s / total_spent) * 100 // 10 * 10) for s in spent_amounts]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"


    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"


    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     "
        for name in [cat.name for cat in categories]:
            chart += (name[i] if i < len(name) else " ") + "  "
        if i < max_len - 1: chart += "\n"

    return chart