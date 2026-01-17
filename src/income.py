class IncomeManager:
    def __init__(self):
        self.incomes = []

    def add_income(self, source, amount):
        self.incomes.append(amount)
        print(f"تمت إضافة دخل من {source} بقيمة {amount}")

    def total_income(self):
        return sum(self.incomes)
