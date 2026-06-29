from abc import ABC, abstractmethod


class BaseAccount(ABC):
    bank_name = "Vietcombank"

    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name.strip().upper()
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __add__(self, other):
        if isinstance(other, BaseAccount):
            return self.balance + other.balance
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BaseAccount):
            return self.balance < other.balance
        return NotImplemented

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_bank_name(cls, new_name):
        cls.bank_name = new_name


class SavingsAccount(BaseAccount):
    def __init__(self, account_number, owner_name, interest_rate, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền nạp không hợp lệ!")
            return
        
        self._set_balance(self.balance + amount)
        print("Nạp tiền thành công!")
        print(f"Số dư hiện tại {self.balance} VND")

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền rút không hợp lệ!")
            return
        
        fee = amount * 0.02
        total = amount + fee

        if self.balance >= total:
            self._set_balance(self.balance - total)
            print("Rút tiền thành công")
            print(f"Phí rút trước hạn {fee} VND")
            print(f"Số dư còn lại: {self.balance} VND")


    def apply_interest(self):
        interest = self.balance + self.interest_rate
        self._set_balance(self.balance + interest)
        print("Tính lãi thành công")
        print(f"Tiền lãi {interest}")
        print(f"Số dư mới {self.balance}")


class CreditAccount(BaseAccount):
    def __init__(self, account_number, owner_name, credit_limit, balance=0):
        super().__init__(account_number, owner_name, balance)
        self.credit_limit = credit_limit
    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền nạp không hợp lệ!")
            return
        
        self._set_balance(self.balance + amount)
        print("Nap tien thanh cong!")
        print(f"So du hien tai: {self.balance:,.0f} VND")

    def withdraw(self, amount):
        if amount <= 0:
            print("So tien rut khong hop le!")
            return

        if self.balance - amount >= -self.credit_limit:
            self._set_balance(self.balance - amount)
            print("Rut tien thanh cong!")
            print(f"So du hien tai: {self.balance:,.0f} VND")
        else:
            print("Vuot qua han muc thau chi!")


class DigitalPremiumMixin:
    @staticmethod
    def cashback_reward(amount):
        if amount > 5000000:
            return amount * 0.01
        return 0


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    def __init__(self, account_number, owner_name, interest_rate, balance=0):
        super().__init__(account_number, owner_name, interest_rate, balance)
def withdraw(self, amount):
        if amount <= 0:
            print("So tien rut khong hop le!")
            return

        if self.balance - amount >= -self.credit_limit:
            self._set_balance(self.balance - amount)
            print("Rut tien thanh cong!")
            print(f"So du hien tai: {self.balance:,.0f} VND")
        else:
            print("Vuot qua han muc thau chi!")


def menu():
    print("\n===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====")
    print("1. Mo tai khoan moi")
    print("2. Xem thong tin tai khoan")
    print("3. Nap / Rut tien")
    print("4. Ap dung lai suat")
    print("5. Tong hop & So sanh tai khoan")
    print("6. Thanh toan hoa don")
    print("7. Thoat")


accounts = []
current_account = None


def open_account():
    print("\n--- CHON LOAI TAI KHOAN ---")
    print("1. Savings Account")
    print("2. Credit Account")
    print("3. Hybrid Account")

    choice = input("Chon loai tai khoan (1-3): ")

    account_number = input("Nhap so tai khoan: ")

    if not BaseAccount.validate_account_number(account_number):
        print("So tai khoan khong hop le!")
        return None

    owner_name = input("Nhap ten chu tai khoan: ")

    if choice == "1":
        interest_rate = float(input("Nhap lai suat: "))
        account = SavingsAccount(account_number, owner_name, interest_rate)

    elif choice == "2":
        credit_limit = float(input("Nhap han muc tin dung: "))
        account = CreditAccount(account_number, owner_name, credit_limit)

    elif choice == "3":
        interest_rate = float(input("Nhap lai suat: "))
        account = HybridAccount(account_number, owner_name, interest_rate)

    else:
        print("Lua chon khong hop le!")
        return None

    print("\nMo tai khoan thanh cong!")
    print("Chu tai khoan:", account.owner_name)

    return account


def show_account(current_account):
    if current_account is None:
        print("He thong chua co thong tin tai khoan!")
        return

    print("\n------ THONG TIN TAI KHOAN ------")
    print("Loai tai khoan:", type(current_account).__name__)
    print("Ngan hang:", current_account.bank_name)
    print("So tai khoan:", current_account.account_number)
    print("Chu tai khoan:", current_account.owner_name)
    print(f"So du: {current_account.balance:,.0f} VND")

    if isinstance(current_account, SavingsAccount):
        print(f"Lai suat: {current_account.interest_rate * 100}%")

    if isinstance(current_account, CreditAccount):
        print(f"Han muc tin dung: {current_account.credit_limit:,.0f} VND")

    print("\nMRO:")
    for cls in current_account.__class__.mro():
        print(cls.__name__)


def transaction(current_account):
    if current_account is None:
        print("He thong chua co tai khoan!")
        return

    print("\n------ GIAO DICH NAP / RUT TIEN ------")
    print("1. Nap tien")
    print("2. Rut tien")

    choice = input("Chon giao dich (1-2): ")

    amount = float(input("Nhap so tien: "))

    if choice == "1":
        current_account.deposit(amount)

        if isinstance(current_account, HybridAccount):
            cashback = current_account.cashback_reward(amount)

            if cashback > 0:
                current_account._set_balance(
                    current_account.balance + cashback)
                print(f"Hoan tien: {cashback:,.0f} VND")
                print(f"So du moi: {current_account.balance:,.0f} VND")

    elif choice == "2":
        current_account.withdraw(amount)

    else:
        print("Lua chon khong hop le!")


def apply_interest(current_account):
    if current_account is None:
        print("He thong chua co tai khoan!")
        return

    if isinstance(current_account, (SavingsAccount, HybridAccount)):
        current_account.apply_interest()
    else:
        print("Tai khoan nay khong ho tro tinh lai!")


def compare_account(accounts, current_account):
    if current_account is None:
        print("He thong chua co tai khoan!")
        return

    if len(accounts) < 2:
        print("Can it nhat 2 tai khoan de so sanh!")
        return

    print("\n------ DANH SACH TAI KHOAN ------")
    for i, account in enumerate(accounts):
        print(f"{i + 1}. {account.owner_name} - {account.account_number}")

    choice = int(input("Chon tai khoan de so sanh: ")) - 1

    if choice < 0 or choice >= len(accounts):
        print("Lua chon khong hop le!")
        return

    other = accounts[choice]

    if other == current_account:
        print("Khong the so sanh cung mot tai khoan!")
        return

    print(f"\nTong so du: {(current_account + other):,.0f} VND")

    if current_account < other:
        print("Tai khoan hien tai co so du nho hon.")
    elif other < current_account:
        print("Tai khoan hien tai co so du lon hon.")
    else:
        print("Hai tai khoan co cung so du.")


def process_payment(gateway, amount):
    gateway.execute_pay(amount)


class ViettelMoneyGateway:
    def execute_pay(self, amount):
        print(f"Thanh toan {amount:,.0f} VND bang Viettel Money thanh cong!")


class VNPayGateway:
    def execute_pay(self, amount):
        print(f"Thanh toan {amount:,.0f} VND bang VNPay thanh cong!")


def payment(current_account):
    if current_account is None:
        print("He thong chua co tai khoan!")
        return

    amount = float(input("Nhap so tien thanh toan: "))

    if amount <= 0:
        print("So tien khong hop le!")
        return

    if current_account.balance < amount:
        print("So du khong du de thanh toan!")
        return

    print("\n1. VNPay")
    print("2. Viettel Money")

    choice = input("Chon cong thanh toan: ")

    if choice == "1":
        gateway = VNPayGateway()

    elif choice == "2":
        gateway = ViettelMoneyGateway()

    else:
        print("Lua chon khong hop le!")
        return

    current_account.withdraw(amount)

    process_payment(gateway, amount)
while True:
    menu()

    choice = input("Chon chuc nang (1-7): ")

    if choice == "1":
        current_account = open_account()

    elif choice == "2":
        show_account(current_account)

    elif choice == "3":
        transaction(current_account)
        
    elif choice == "4":
        apply_interest(current_account)
        
    elif choice == "5":
        compare_account(accounts, current_account)
        
    elif choice == "6":
        payment(current_account)
        pass
    elif choice == "7":
            print("Cam on da su dung chuong trinh!")
            break

    else:
        print("Lua chon khong hop le!")
