class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__account_name = account_name.strip().upper()
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        new_name = new_name.strip()

        if new_name == "":
            print("Tên tài khoản không được để trống")
            return

        self.__account_name = new_name.upper()

    @staticmethod
    def validate_account_number(account_number):
        return (
            account_number.isdigit()
            and len(account_number) == 10
        )

    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        total = amount + BankAccount.transaction_fee

        if self.__balance < total:
            print(
                "Giao dịch thất bại. "
                "Số dư không đủ để thanh toán số tiền và phí giao dịch"
            )
            return False

        self.__balance -= total
        return True

    def display_info(self):
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.__account_number}")
        print(f"Tên chủ tài khoản: {self.__account_name}")
        print(f"Số dư hiện tại: {self.__balance:,} VND")
        print(
            f"Phí giao dịch: "
            f"{BankAccount.transaction_fee:,} VND"
        )


current_account = None

while True:
    print("""
===== VIETCOMBANK DIGIBANK SIMULATOR =====
1. Mở tài khoản mới
2. Xem thông tin tài khoản
3. Giao dịch Nạp / Rút tiền
4. Cập nhật Tên chủ tài khoản
5. Đổi phí giao dịch hệ thống
6. Thoát chương trình
==========================================
""")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("--- MỞ TÀI KHOẢN MỚI ---")

        while True:
            account_number = input(
                "Nhập số tài khoản 10 chữ số: "
            )

            if BankAccount.validate_account_number(
                account_number
            ):
                break

            print("Số tài khoản không hợp lệ!")
            print(
                "Số tài khoản phải gồm đúng 10 chữ số."
            )

        account_name = input(
            "Nhập tên chủ tài khoản: "
        )

        current_account = BankAccount(
            account_number,
            account_name
        )

        print("Mở tài khoản thành công!")
        print(
            f"Số tài khoản: "
            f"{account_number}"
        )
        print(
            f"Tên chủ tài khoản: "
            f"{current_account.account_name}"
        )

    elif choice == "2":
        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print(
                "Vui lòng mở tài khoản "
                "ở Chức năng 1 trước."
            )
        else:
            print(
                "--- THÔNG TIN TÀI KHOẢN ---"
            )
            current_account.display_info()

    elif choice == "3":
        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print(
                "Vui lòng mở tài khoản "
                "ở Chức năng 1 trước."
            )
            continue

        print("""
--- GIAO DỊCH NẠP / RÚT TIỀN ---
1. Nạp tiền
2. Rút tiền
""")

        transaction_choice = input(
            "Chọn loại giao dịch (1-2): "
        )

        try:
            amount = int(
                input("Nhập số tiền giao dịch: ")
            )
        except ValueError:
            print("Số tiền không hợp lệ")
            continue

        if transaction_choice == "1":
            if current_account.deposit(amount):
                print(
                    f"Nạp tiền thành công: "
                    f"+{amount:,} VND"
                )
                print(
                    f"Số dư mới: "
                    f"{current_account.balance:,} VND"
                )

        elif transaction_choice == "2":
            if current_account.withdraw(amount):
                print(
                    f"Rút tiền thành công: "
                    f"-{amount:,} VND"
                )
                print(
                    f"Phí giao dịch: "
                    f"{BankAccount.transaction_fee:,} VND"
                )
                print(
                    f"Số dư mới: "
                    f"{current_account.balance:,} VND"
                )
            else:
                print(
                    f"Số dư mới: "
                    f"{current_account.balance:,} VND"
                )

        else:
            print("Lựa chọn không hợp lệ")

    elif choice == "4":
        if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản")
            print(
                "Vui lòng mở tài khoản "
                "ở Chức năng 1 trước."
            )
        else:
            print(
                "--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---"
            )

            new_name = input(
                "Nhập tên mới: "
            )

            old_name = current_account.account_name

            current_account.account_name = new_name

            if current_account.account_name != old_name:
                print(
                    f"Cập nhật thành công. "
                    f"Tên mới: "
                    f"{current_account.account_name}"
                )

    elif choice == "5":
        print(
            "--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---"
        )

        print(
            f"Phí giao dịch hiện tại: "
            f"{BankAccount.transaction_fee:,} VND"
        )

        try:
            new_fee = int(
                input(
                    "Nhập phí giao dịch mới: "
                )
            )

            if new_fee < 0:
                print(
                    "Phí giao dịch không được âm"
                )
                print(
                    f"Phí giao dịch hiện tại vẫn là "
                    f"{BankAccount.transaction_fee:,} VND"
                )
            else:
                BankAccount.update_transaction_fee(
                    new_fee
                )

                print(
                    f"Đã cập nhật phí giao dịch "
                    f"toàn hệ thống thành "
                    f"{new_fee:,} VND"
                )

        except ValueError:
            print(
                "Phí giao dịch không hợp lệ"
            )

    elif choice == "6":
        print(
            "Cảm ơn bạn đã sử dụng "
            "Vietcombank Digibank!"
        )
        break

    else:
        print("Lựa chọn không hợp lệ")
