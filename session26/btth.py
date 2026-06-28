from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        print(
            f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: {self.employee_type}")

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    employee_type = "Full-time"

    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    employee_type = "Part-time"

    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.working_hours * self.hourly_rate


class InternEmployee(Employee):
    employee_type = "Intern"

    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance

    def calculate_salary(self):
        return self.allowance


employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
]


def display_employees(employees):
    print("\n--- DANH SÁCH NHÂN VIÊN ---")
    for employee in employees:
        employee.display_info()


def display_salaries(employees):
    print("\n--- BẢNG LƯƠNG NHÂN VIÊN ---")
    for employee in employees:
        salary = employee.calculate_salary()
        print(f"{employee.employee_id} | {employee.name} | Lương: {salary:,.0f} VND")


while True:
    print("""
=== EMPLOYEE SALARY MANAGER ===
1. Xem danh sách nhân viên
2. Tính lương toàn bộ nhân viên
3. Thoát chương trình
================================
""")

    choice = input("Chọn chức năng (1-3): ")

    if choice == "1":
        display_employees(employees)

    elif choice == "2":
        display_salaries(employees)

    elif choice == "3":
        print("Cảm ơn bạn đã sử dụng Employee Salary Manager!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
