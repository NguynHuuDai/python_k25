class NetflixAccount:
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

    @property
    def plan(self):
        return self.__plan

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        cls.max_profiles = new_limit

    def add_profile(self, profile_name):
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print(
                "Đã đạt giới hạn số lượng Profile "
                "trên tài khoản này"
            )
            return

        self.profiles.append(profile_name)
        print("Thêm Profile thành công!")

    def upgrade_plan(self, new_plan):
        valid_plans = [
            "Basic",
            "Standard",
            "Premium"
        ]

        if new_plan in valid_plans:
            self.__plan = new_plan
            print(
                f"Nâng cấp gói cước thành công: "
                f"{new_plan}"
            )
        else:
            print("Gói cước không hợp lệ!")

    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Platform: {NetflixAccount.platform_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Plan: {self.plan}")

        if len(self.profiles) == 0:
            print("Profiles: Chưa có profile nào")
        else:
            print(
                "Profiles:",
                ", ".join(self.profiles)
            )


current_account = None

while True:
    print("""
===== NETFLIX ACCOUNT MANAGER =====
1. Đăng ký tài khoản mới
2. Xem thông tin tài khoản
3. Thêm người xem
4. Nâng cấp gói cước
5. Cập nhật chính sách Netflix
6. Thoát chương trình
===================================
""")

    choice = input(
        "Chọn chức năng (1-6): "
    )

    if choice == "1":
        print(
            "\n--- ĐĂNG KÝ TÀI KHOẢN MỚI ---"
        )

        while True:
            email = input("Nhập email: ")

            if NetflixAccount.validate_email(
                email
            ):
                break

            print(
                "Email không hợp lệ, "
                "vui lòng chứa ký tự '@' và '.'"
            )

        account = NetflixAccount(email)

        while True:
            try:
                password = input(
                    "Nhập mật khẩu: "
                )

                account.password = password
                break

            except ValueError as e:
                print(e)

        current_account = account

        print(
            "Đăng ký tài khoản thành công!"
        )

    elif choice == "2":
        if current_account is None:
            print(
                "Vui lòng đăng ký tài khoản trước "
                "(Chức năng 1)"
            )
        else:
            current_account.display_info()

    elif choice == "3":
        if current_account is None:
            print(
                "Vui lòng đăng ký tài khoản trước "
                "(Chức năng 1)"
            )
        else:
            profile_name = input(
                "Nhập tên profile: "
            )

            current_account.add_profile(
                profile_name
            )

    elif choice == "4":
        if current_account is None:
            print(
                "Vui lòng đăng ký tài khoản trước "
                "(Chức năng 1)"
            )
        else:
            print("""
1. Basic
2. Standard
3. Premium
""")

            plan_choice = input(
                "Chọn gói cước: "
            )

            if plan_choice == "1":
                current_account.upgrade_plan(
                    "Basic"
                )

            elif plan_choice == "2":
                current_account.upgrade_plan(
                    "Standard"
                )

            elif plan_choice == "3":
                current_account.upgrade_plan(
                    "Premium"
                )

            else:
                print(
                    "Lựa chọn không hợp lệ!"
                )

    elif choice == "5":
        try:
            new_limit = int(
                input(
                    "Nhập giới hạn profile mới: "
                )
            )

            if new_limit <= 0:
                print(
                    "Giới hạn phải lớn hơn 0"
                )
            else:
                NetflixAccount.update_max_profiles(
                    new_limit
                )

                print(
                    f"Đã cập nhật giới hạn "
                    f"Profile toàn hệ thống thành "
                    f"{new_limit}"
                )

        except ValueError:
            print(
                "Dữ liệu nhập không hợp lệ"
            )

    elif choice == "6":
        print(
            "Cảm ơn bạn đã sử dụng "
            "Netflix Account Manager!"
        )
        break

    else:
        print("Lựa chọn không hợp lệ!")