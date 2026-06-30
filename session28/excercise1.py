from abc import ABC, abstractmethod


class BaseEmployee(ABC):
    company_name = "Rikkei Education"
    base_salary_rate = 3000000

    def __init__(self, emp_code, full_name):
        self.emp_code = emp_code
        self.full_name = full_name
        self.__working_hours = 0

    @property
    def working_hours(self):
        return self.__working_hours

    def _add_working_hours(self, hours):
        if hours <= 0:
            raise ValueError("Working hours must be greater than 0.")
        self.__working_hours += hours

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = " ".join(value.strip().upper().split())

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def update_kpi(self, progress):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.working_hours + other.working_hours

    def __lt__(self, other):
        if not isinstance(other, BaseEmployee):
            return NotImplemented
        return self.working_hours < other.working_hours

    @staticmethod
    def validate_employee_code(emp_code):
        return len(emp_code) == 10 and emp_code.startswith("RKE")

    @classmethod
    def update_base_salary_rate(cls, new_rate):
        if new_rate <= 0:
            raise ValueError("Base salary must be greater than 0.")
        cls.base_salary_rate = new_rate


class Lecturer(BaseEmployee):
    def __init__(self, emp_code, full_name, teaching_slots=0):
        super().__init__(emp_code, full_name)
        self.teaching_slots = teaching_slots
        self.kpi = 0

    def conduct_class(self):
        self.teaching_slots += 1
        self._add_working_hours(2)

    def calculate_salary(self):
        return (
            self.working_hours * self.base_salary_rate
            + self.teaching_slots * 500000
        )

    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError(
                "So lieu cap nhat hieu suat khong duoc nho hon hoac bang 0."
            )

        self.kpi = progress

    def display_info(self):
        print("Loai nhan su: Lecturer")
        print("To chuc:", self.company_name)
        print("Ma nhan su:", self.emp_code)
        print("Ho ten:", self.full_name)
        print("So gio lam:", self.working_hours)
        print("So ca day:", self.teaching_slots)
        print("KPI:", self.kpi)


class AdmissionStaff(BaseEmployee):
    def __init__(
        self,
        emp_code,
        full_name,
        revenue_generated=0,
        kpi_target=100000000
    ):
        super().__init__(emp_code, full_name)
        self.revenue_generated = revenue_generated
        self.kpi_target = kpi_target

    def calculate_salary(self):
        return (
            self.working_hours * self.base_salary_rate
            + self.revenue_generated * 0.05
        )

    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError(
                "So lieu cap nhat hieu suat khong duoc nho hon hoac bang 0."
            )

        self.revenue_generated += progress

    def display_info(self):
        print("Loai nhan su: AdmissionStaff")
        print("To chuc:", self.company_name)
        print("Ma nhan su:", self.emp_code)
        print("Ho ten:", self.full_name)
        print("So gio lam:", self.working_hours)
        print("Doanh so:", format(self.revenue_generated, ","))
        print("Chi tieu:", format(self.kpi_target, ","))


class HybridManager(Lecturer, AdmissionStaff):
    def __init__(
        self,
        emp_code,
        full_name,
        teaching_slots=0,
        revenue_generated=0,
        kpi_target=100000000
    ):
        Lecturer.__init__(
            self,
            emp_code,
            full_name,
            teaching_slots
        )

        self.revenue_generated = revenue_generated
        self.kpi_target = kpi_target

    def calculate_salary(self):
        basic_salary = self.working_hours * self.base_salary_rate
        teaching_bonus = self.teaching_slots * 500000
        commission = self.revenue_generated * 0.05

        return basic_salary + teaching_bonus + commission

    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError(
                "So lieu cap nhat hieu suat khong duoc nho hon hoac bang 0."
            )

        self.revenue_generated += progress

    def display_info(self):
        print("Loai nhan su: HybridManager")
        print("To chuc:", self.company_name)
        print("Ma nhan su:", self.emp_code)
        print("Ho ten:", self.full_name)
        print("So gio lam:", self.working_hours)
        print("So ca day:", self.teaching_slots)
        print("Doanh so:", format(self.revenue_generated, ","))
        print("Chi tieu:", format(self.kpi_target, ","))

    def show_mro(self):
        for cls in HybridManager.__mro__:
            print(cls.__name__)


class VietcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print("[He thong VCB Corporate]: Dang ket noi...")
        print("Xac thuc Duck Typing thanh cong!")
        print(
            "Da giai ngan",
            format(amount, ","),
            "VND toi",
            employee.emp_code
        )


class TechcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print("[He thong TCB Corporate]: Dang ket noi...")
        print("Xac thuc Duck Typing thanh cong!")
        print(
            "Da giai ngan",
            format(amount, ","),
            "VND toi",
            employee.emp_code
        )


def execute_payroll(payment_service, employee, amount):
    try:
        payment_service.transfer_salary(employee, amount)
    except AttributeError:
        print(
            "Cong dich vu ngan hang doanh nghiep khong hop le hoac chua duoc lien ket."
        )


employees = []
current_employee = None


def recruit_employee():
    global current_employee

    print("\n--- CHON LOAI NHAN SU KHOI TAO ---")
    print("1. Lecturer")
    print("2. Admission Staff")
    print("3. Hybrid Manager")

    try:
        choice = int(input("Chon loai nhan su (1-3): "))
    except ValueError:
        print("Lua chon khong hop le.")
        return

    emp_code = input("Nhap ma nhan su 10 ky tu: ").strip()

    if not BaseEmployee.validate_employee_code(emp_code):
        print("Ma nhan su khong hop le!")
        return

    full_name = input("Nhap ho va ten: ")

    if choice == 1:
        employee = Lecturer(emp_code, full_name)

    elif choice == 2:
        employee = AdmissionStaff(emp_code, full_name)

    elif choice == 3:
        employee = HybridManager(emp_code, full_name)

    else:
        print("Loai nhan su khong ton tai.")
        return

    employees.append(employee)
    current_employee = employee

    print("Tuyen dung thanh cong!")
    print("Ten nhan su:", current_employee.full_name)


def show_current_employee():
    if current_employee is None:
        print("Chua co nhan su nao.")
        return

    print("\n--- THONG TIN NHAN SU ---")
    current_employee.display_info()

    print("\n--- MRO ---")

    for cls in type(current_employee).__mro__:
        print(cls.__name__)


def choose_employee():
    if len(employees) == 0:
        print("Danh sach rong.")
        return None

    print("\nDanh sach nhan su:")

    for i in range(len(employees)):
        print(
            i + 1,
            employees[i].emp_code,
            employees[i].full_name
        )

    try:
        index = int(input("Chon nhan su: ")) - 1

        if index < 0 or index >= len(employees):
            print("Lua chon khong hop le.")
            return None

        return employees[index]

    except ValueError:
        print("Du lieu khong hop le.")
        return None


def update_employee():
    if current_employee is None:
        print("Chua co nhan su nao.")
        return

    print("\n--- GHI NHAN CONG NHAT & HIEU SUAT ---")
    print("1. Ghi nhan tham gia dung lop")
    print("2. Cap nhat KPI / Doanh so")

    try:
        choice = int(input("Chon tac vu: "))
    except ValueError:
        print("Du lieu khong hop le.")
        return

    if choice == 1:
        if isinstance(current_employee, (Lecturer, HybridManager)):
            try:
                current_employee.conduct_class()
                print("Ghi nhan thanh cong!")
                print("So ca day:", current_employee.teaching_slots)
                print("So gio lam:", current_employee.working_hours)
            except ValueError as e:
                print(e)
        else:
            print("Nhan su nay khong the dung lop.")

    elif choice == 2:
        try:
            progress = float(input("Nhap gia tri KPI / Doanh so: "))
            current_employee.update_kpi(progress)
            print("Cap nhat thanh cong!")

            if isinstance(current_employee, Lecturer):
                print("KPI:", current_employee.kpi)

            if isinstance(current_employee, (AdmissionStaff, HybridManager)):
                print(
                    "Doanh so:",
                    format(current_employee.revenue_generated, ",")
                )

        except ValueError as e:
            print(e)

    else:
        print("Lua chon khong hop le.")


def payroll_summary():
    if current_employee is None:
        print("Chua co nhan su nao.")
        return

    salary = current_employee.calculate_salary()

    print("\n--- CHI TIET QUY LUONG ---")
    print("Nhan su:", current_employee.full_name)
    print("Loai:", type(current_employee).__name__)
    print(
        "Luong co so:",
        format(BaseEmployee.base_salary_rate, ","),
        "VND"
    )
    print(
        "So gio lam:",
        current_employee.working_hours
    )

    if isinstance(current_employee, (Lecturer, HybridManager)):
        print(
            "So ca day:",
            current_employee.teaching_slots
        )

    if isinstance(current_employee, (AdmissionStaff, HybridManager)):
        print(
            "Doanh so:",
            format(current_employee.revenue_generated, ",")
        )

    print(
        "Tong luong:",
        format(salary, ","),
        "VND"
    )


def compare_employee():
    if current_employee is None:
        print("Chua co nhan su nao.")
        return

    if len(employees) < 2:
        print("Can it nhat 2 nhan su.")
        return

    other = choose_employee()

    if other is None:
        return

    if other == current_employee:
        print("Khong the so sanh voi chinh minh.")
        return

    try:
        if current_employee < other:
            print("Nhan su hien tai co it gio lam hon.")
        else:
            print("Nhan su hien tai co nhieu hoac bang gio lam.")

        total = current_employee + other

        print("Tong gio lam:", total)

    except TypeError:
        print("Khong the thuc hien phep so sanh.")


def payroll_transfer():
    if current_employee is None:
        print("Chua co nhan su nao.")
        return

    print("\n1. Vietcombank")
    print("2. Techcombank")

    try:
        choice = int(input("Chon ngan hang: "))
        amount = float(input("Nhap so tien giai ngan: "))
    except ValueError:
        print("Du lieu khong hop le.")
        return

    if choice == 1:
        service = VietcombankCorporateService()

    elif choice == 2:
        service = TechcombankCorporateService()

    else:
        print("Lua chon khong hop le.")
        return

    execute_payroll(service, current_employee, amount)


def show_menu():
    print("\n========== RIKKEI HR ==========")
    print("1. Tuyen dung nhan su")
    print("2. Xem thong tin")
    print("3. Ghi nhan cong nhat & KPI")
    print("4. Tong hop quy luong")
    print("5. Overloading")
    print("6. Giai ngan luong")
    print("7. Thoat")
    print("===============================")


while True:
    show_menu()

    try:
        choice = int(input("Chon chuc nang: "))
    except ValueError:
        print("Du lieu khong hop le.")
        continue

    if choice == 1:
        recruit_employee()

    elif choice == 2:
        show_current_employee()

    elif choice == 3:
        update_employee()

    elif choice == 4:
        payroll_summary()

    elif choice == 5:
        compare_employee()

    elif choice == 6:
        payroll_transfer()

    elif choice == 7:
        print("Cam on da su dung chuong trinh.")
        break

    else:
        print("Lua chon khong hop le.")
