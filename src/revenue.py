# ملف إدارة الأرباح

class RevenueManager:
    def __init__(self):
        self.revenues = []

    def add_revenue(self, amount):
        self.revenues.append(amount)

    def total_revenue(self):
        return sum(self.revenues)
