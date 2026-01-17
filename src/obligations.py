
# ملف إدارة الالتزامات المالية

class Obligation:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


class ObligationsManager:
    def __init__(self):
        self.obligations = []

    def add_obligation(self, name, amount):
        obligation = Obligation(name, amount)
        self.obligations.append(obligation)

    def total_obligations(self):
        return sum(o.amount for o in self.obligations)
