from income import IncomeManager

from obligations import ObligationsManager
print("Smart Accounting Bot is starting 🚀")


manager = ObligationsManager
income_manager = IncomeManager()

print("مرحبا بك في المحاسب المالي الذكي 🤖")

while True:
    name = input("ادخلي اسم الالتزام (او اكتبي خروج): ")
    if name == "خروج":
        break

    amount = float(input("ادخلي المبلغ: "))
    manager.add_obligation(name, amount)

print("إجمالي الالتزامات:", manager.total_obligation
Smart-Accounting-Assistant
└── src
    ├── main.py          ← التشغيل
    ├── obligations.py  ← الالتزامات
    └── income.py       ← الأرباح
