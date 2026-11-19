# Management system
# Python program
# Records stay available until the program is closed.

expenses = []
attendance = []
students = []
bills = []

categories = ["Food", "Travel", "Utilities", "Stationery", "Other"]


# Input functions

def read_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def read_whole_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a whole number.")


def read_name(message):
    while True:
        name = input(message).strip()
        if len(name) >= 2 and name.replace(" ", "").isalpha():
            return name
        print("Please enter a valid name.")


def line():
    print("-" * 55)


# Expense management

def add_expense():
    print("\nADD EXPENSE")
    description = input("Enter expense description: ").strip()

    print("Categories:", ", ".join(categories))
    category = input("Enter category: ").strip().title()

    if category not in categories:
        print("Invalid category.")
        return

    amount = read_number("Enter amount: ")
    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    expenses.append({
        "description": description,
        "category": category,
        "amount": round(amount, 2)
    })
    print("Expense added successfully.")


def show_expenses():
    print("\nEXPENSE REPORT")
    if len(expenses) == 0:
        print("No expense records found.")
        return

    total = 0
    category_total = {}

    line()
    print(f"{'Description':20} {'Category':15} {'Amount':>10}")
    line()

    for item in expenses:
        print(f"{item['description'][:20]:20} "
              f"{item['category']:15} {item['amount']:10.2f}")
        total += item["amount"]
        category_total[item["category"]] = (
            category_total.get(item["category"], 0) + item["amount"]
        )

    line()
    print(f"Total expense: Rs. {total:.2f}")
    print("\nCategory-wise total:")
    for category, amount in category_total.items():
        print(f"{category}: Rs. {amount:.2f}")

    highest = max(expenses, key=lambda x: x["amount"])
    lowest = min(expenses, key=lambda x: x["amount"])
    print(f"Highest expense: {highest['description']} - Rs. {highest['amount']:.2f}")
    print(f"Lowest expense: {lowest['description']} - Rs. {lowest['amount']:.2f}")


def expense_menu():
    while True:
        print("\n1. Add expense")
        print("2. View expense report")
        print("3. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


# Attendance management

def add_attendance():
    print("\nADD ATTENDANCE")
    name = read_name("Enter student/employee name: ")
    total_days = read_whole_number("Enter total working days: ")

    if total_days < 1:
        print("Total working days must be at least 1.")
        return

    present_days = read_whole_number("Enter days present: ")
    if present_days < 0 or present_days > total_days:
        print("Present days must be between 0 and total working days.")
        return

    percentage = (present_days / total_days) * 100

    if percentage >= 75:
        status = "Eligible"
    elif percentage >= 60:
        status = "Warning"
    else:
        status = "Shortage"

    attendance.append({
        "name": name,
        "total": total_days,
        "present": present_days,
        "percentage": percentage,
        "status": status
    })

    print(f"Attendance: {percentage:.2f}%")
    print("Status:", status)


def show_attendance():
    print("\nATTENDANCE REPORT")
    if len(attendance) == 0:
        print("No attendance records found.")
        return

    line()
    print(f"{'Name':18} {'Total':>7} {'Present':>8} {'Percent':>10} {'Status':>12}")
    line()

    percentages = []
    eligible = 0
    warning = 0
    shortage = 0

    for record in attendance:
        print(f"{record['name'][:18]:18} {record['total']:7} "
              f"{record['present']:8} {record['percentage']:9.2f}% "
              f"{record['status']:>12}")
        percentages.append(record["percentage"])

        if record["status"] == "Eligible":
            eligible += 1
        elif record["status"] == "Warning":
            warning += 1
        else:
            shortage += 1

    line()
    print(f"Total people: {len(attendance)}")
    print(f"Average attendance: {sum(percentages) / len(percentages):.2f}%")
    print(f"Highest attendance: {max(percentages):.2f}%")
    print(f"Lowest attendance: {min(percentages):.2f}%")
    print(f"Eligible: {eligible}, Warning: {warning}, Shortage: {shortage}")


def attendance_menu():
    while True:
        print("\n1. Add attendance")
        print("2. View attendance report")
        print("3. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            add_attendance()
        elif choice == "2":
            show_attendance()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


# Grading system

def find_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 35:
        return "E"
    else:
        return "F"


def add_student_marks():
    print("\nENTER STUDENT MARKS")
    name = read_name("Enter student name: ")

    subject_input = input("Number of subjects (press Enter for 5): ").strip()
    if subject_input == "":
        subject_count = 5
    else:
        try:
            subject_count = int(subject_input)
        except ValueError:
            print("Enter a valid whole number.")
            return

    if subject_count < 1 or subject_count > 20:
        print("Number of subjects must be between 1 and 20.")
        return

    subjects = []
    marks = []

    for i in range(subject_count):
        subject = input(f"Enter subject {i + 1} name: ").strip()
        if subject == "":
            print("Subject name cannot be empty.")
            return

        mark = read_number(f"Enter marks for {subject}: ")
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return

        subjects.append(subject)
        marks.append(mark)

    total = sum(marks)
    percentage = total / subject_count
    grade = find_grade(percentage)

    if min(marks) < 35:
        result = "FAIL"
    else:
        result = "PASS"

    student = {
        "name": name,
        "subjects": subjects,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }
    students.append(student)
    show_report_card(student)


def show_report_card(student):
    print("\nSTUDENT REPORT CARD")
    line()
    print("Student:", student["name"])
    for subject, mark in zip(student["subjects"], student["marks"]):
        print(f"{subject}: {mark:.2f}")

    line()
    print(f"Total: {student['total']:.2f} / {len(student['marks']) * 100}")
    print(f"Average: {student['percentage']:.2f}")
    print(f"Percentage: {student['percentage']:.2f}%")
    print("Grade:", student["grade"])
    print("Result:", student["result"])


def show_grading_report():
    print("\nCLASS RESULT")
    if len(students) == 0:
        print("No student records found.")
        return

    percentages = []
    passed = 0
    failed = 0

    line()
    print(f"{'Name':20} {'Percentage':>12} {'Grade':>8} {'Result':>8}")
    line()

    for student in students:
        print(f"{student['name'][:20]:20} {student['percentage']:11.2f}% "
              f"{student['grade']:>8} {student['result']:>8}")
        percentages.append(student["percentage"])

        if student["result"] == "PASS":
            passed += 1
        else:
            failed += 1

    line()
    print(f"Class average: {sum(percentages) / len(percentages):.2f}%")
    print("Highest percentage:", f"{max(percentages):.2f}%")
    print("Pass count:", passed)
    print("Fail count:", failed)


def grading_menu():
    while True:
        print("\n1. Enter student marks")
        print("2. View class report")
        print("3. View a student report card")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student_marks()
        elif choice == "2":
            show_grading_report()
        elif choice == "3":
            if len(students) == 0:
                print("No student records found.")
            else:
                for i, student in enumerate(students, start=1):
                    print(f"{i}. {student['name']}")
                number = read_whole_number("Select student number: ")
                if 1 <= number <= len(students):
                    show_report_card(students[number - 1])
                else:
                    print("Invalid student number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


# Billing system

def add_bill():
    print("\nCREATE BILL")
    customer = read_name("Enter customer name: ")
    items = []

    while True:
        item_name = input("Enter item name (or type done): ").strip()
        if item_name.lower() == "done":
            break
        if item_name == "":
            print("Item name cannot be empty.")
            continue

        price = read_number("Enter unit price: ")
        quantity = read_whole_number("Enter quantity: ")

        if price <= 0 or quantity < 1:
            print("Price must be above zero and quantity at least 1.")
            continue

        items.append({
            "name": item_name,
            "price": price,
            "quantity": quantity,
            "total": price * quantity
        })

    if len(items) == 0:
        print("No items entered. Bill not created.")
        return

    subtotal = sum(item["total"] for item in items)

    if subtotal >= 10000:
        discount_rate = 0.15
    elif subtotal >= 5000:
        discount_rate = 0.10
    elif subtotal >= 1000:
        discount_rate = 0.05
    else:
        discount_rate = 0

    discount = subtotal * discount_rate
    taxable_amount = subtotal - discount
    tax = taxable_amount * 0.18
    grand_total = taxable_amount + tax

    bill = {
        "number": len(bills) + 1,
        "customer": customer,
        "items": items,
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "grand_total": grand_total
    }
    bills.append(bill)
    show_bill(bill)


def show_bill(bill):
    print("\nCUSTOMER INVOICE")
    line()
    print("Bill number:", bill["number"])
    print("Customer:", bill["customer"])
    line()
    print(f"{'Item':20} {'Price':>9} {'Qty':>6} {'Total':>10}")

    for item in bill["items"]:
        print(f"{item['name'][:20]:20} {item['price']:9.2f} "
              f"{item['quantity']:6} {item['total']:10.2f}")

    line()
    print(f"Subtotal: Rs. {bill['subtotal']:.2f}")
    print(f"Discount: Rs. {bill['discount']:.2f}")
    print(f"GST (18%): Rs. {bill['tax']:.2f}")
    print(f"GRAND TOTAL: Rs. {bill['grand_total']:.2f}")
    line()


def show_billing_report():
    print("\nBILLING REPORT")
    if len(bills) == 0:
        print("No bills found.")
        return

    total = 0
    for bill in bills:
        print(f"Bill {bill['number']} | {bill['customer']} | "
              f"Rs. {bill['grand_total']:.2f}")
        total += bill["grand_total"]

    print(f"Total bills: {len(bills)}")
    print(f"Total sales: Rs. {total:.2f}")


def billing_menu():
    while True:
        print("\n1. Create bill")
        print("2. View billing report")
        print("3. View an invoice")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            add_bill()
        elif choice == "2":
            show_billing_report()
        elif choice == "3":
            if len(bills) == 0:
                print("No bills found.")
            else:
                for bill in bills:
                    print(f"{bill['number']}. {bill['customer']}")
                number = read_whole_number("Enter bill number: ")
                if 1 <= number <= len(bills):
                    show_bill(bills[number - 1])
                else:
                    print("Invalid bill number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


# Reports

def reports_menu():
    while True:
        print("\nREPORTS")
        print("1. Expense report")
        print("2. Attendance report")
        print("3. Grading report")
        print("4. Billing report")
        print("5. All reports")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            show_expenses()
        elif choice == "2":
            show_attendance()
        elif choice == "3":
            show_grading_report()
        elif choice == "4":
            show_billing_report()
        elif choice == "5":
            show_expenses()
            show_attendance()
            show_grading_report()
            show_billing_report()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


# Main menu

def main():
    while True:
        print("\n======================================")
        print(" EXPENSE | ATTENDANCE | GRADING | BILLING")
        print("======================================")
        print("1. Expense Management")
        print("2. Attendance Management")
        print("3. Grading System")
        print("4. Billing System")
        print("5. View Reports")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            expense_menu()
        elif choice == "2":
            attendance_menu()
        elif choice == "3":
            grading_menu()
        elif choice == "4":
            billing_menu()
        elif choice == "5":
            reports_menu()
        elif choice == "6":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please enter 1-6.")


main()
