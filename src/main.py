
from income import IncomeManager
from obligations import ObligationsManager

print("🤖 مرحباً بك في المحاسب المالي الذكي")

income_manager = IncomeManager()
obligations_manager = ObligationsManager()


while True:
    print("اختر عملية:")
    print("1 - إضافة دخل")
    print("2 - إضافة التزام")
    print("3 - عرض الملخص")
    print("4 - خروج")

    choice = input("اختيارك: ")

    if choice == "1":
        source = input("مصدر الدخل: ")
        amount = float(input("المبلغ: "))
        income_manager.add_income(source, amount)

    elif choice == "2":
        name = input("اسم الالتزام: ")
        amount = float(input("المبلغ: "))
        obligations_manager.add_obligation(name, amount)

    elif choice == "3":
        print("💰 إجمالي الدخل:", income_manager.total_income())

    elif choice == "4":
        print("👋 تم الخروج، بالتوفيق")
        break

    else:
        print("❌ اختيار غير صحيح")
