class IncomeManager:
    def __init__(self):
        self.incomes = []

    def add_income(self, source, amount):
        self.incomes.append({
            "source": source,
            "amount": amount
        })

    def total_income(self):
        return sum(item["amount"] for item in self.incomes)
