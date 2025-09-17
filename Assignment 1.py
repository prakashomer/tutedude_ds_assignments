employees = {
    101: {"name": "Satya", "age": 27, "department": "HR", "salary": 50000},
    102: {"name": "Anita", "age": 30, "department": "IT", "salary": 60000},
}

def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("🙏 Thank you for using EMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def add_employee():
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Try again with a new ID.")
            return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employees[emp_id] = {
            "name": name,
            "age": age,
            "department": department,
            "salary": salary,
        }
        print("Employee {name} added successfully!")

def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\n--- Employee List ---")
    print(f"{'ID':<6}{'Name':<15}{'Age':<6}{'Department':<12}{'Salary':<10}")
    print("-" * 50)
    for emp_id, details in employees.items():
        print(
            f"{emp_id:<6}{details['name']:<15}{details['age']:<6}{details['department']:<12}{details['salary']:<10.2f}"
        )
    print()


def search_employee():
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print("\n--- Employee Found ---")
            print(f"ID: {emp_id}")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}")
        else:
            print("Employee not found.")


if __name__ == "__main__":
    main_menu()
