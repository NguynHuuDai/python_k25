import re


class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, value):
        if value <= 0:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")
        else:
            self.__base_price = value

    @property
    def is_available(self):
        return self.__is_available

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def calculate_selling_price(self):
        return self.__base_price + (
            self.__base_price * MenuItem.service_charge
        )

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_code):
        pattern = r"^[A-Z]{2}[0-9]{2}$"
        return re.match(pattern, item_code) is not None


menu_db = [
    MenuItem("CF01", "Ca Phe Den", 30000),
    MenuItem("CF02", "Bac Xiu", 45000),
    MenuItem("TE01", "Tra Dao Cam Sa", 50000)
]


while True:
    print("\n===== HE THONG QUAN LY THUC DON RIKKEI COFFEE =====")
    print("1. Xem thuc don & Gia niem yet")
    print("2. Them mon moi vao menu")
    print("3. Cap nhat trang thai (Het hang/Con hang)")
    print("4. Dieu chinh gia goc cua mon")
    print("5. Cap nhat phu phi dich vu toan he thong")
    print("6. Thoat chuong trinh")
    print("===================================================")

    choice = input("Chon chuc nang (1-6): ")

    if choice == "1":
        print("\n--- THUC DON RIKKEI COFFEE ---")

        for index, item in enumerate(menu_db, start=1):
            status = (
                "Dang ban"
                if item.is_available
                else "Het hang"
            )

            print(
                f"{index}. Ma: {item.item_id} | "
                f"Ten: {item.item_name} | "
                f"Trang thai: {status} | "
                f"Gia niem yet: {item.calculate_selling_price():,.0f} VND"
            )

    elif choice == "2":
        print("\n--- THEM MON MOI VAO MENU ---")

        item_id = input("Nhap ma mon: ")

        if not MenuItem.is_valid_item_id(item_id):
            print("Ma mon khong hop le!")
            print(
                "Ma mon phai gom 2 chu cai in hoa va 2 chu so. "
                "Vi du: CF01."
            )
            continue

        duplicated = False

        for item in menu_db:
            if item.item_id == item_id:
                duplicated = True
                break

        if duplicated:
            print("Ma mon da ton tai!")
            continue

        item_name = input("Nhap ten mon: ")

        try:
            base_price = float(
                input("Nhap gia goc: ")
            )

            if base_price <= 0:
                print("Gia do uong phai lon hon 0!")
                continue

        except ValueError:
            print("Gia khong hop le!")
            continue

        new_item = MenuItem(
            item_id,
            item_name,
            base_price
        )

        menu_db.append(new_item)

        print("Them mon moi thanh cong!")

    elif choice == "3":
        print("\n--- CAP NHAT TRANG THAI MON ---")

        item_id = input(
            "Nhap ma mon can cap nhat: "
        )

        found = False

        for item in menu_db:
            if item.item_id == item_id:
                item.toggle_availability()

                status = (
                    "DANG BAN"
                    if item.is_available
                    else "HET HANG"
                )

                print(
                    f">> Da cap nhat "
                    f"{item.item_name} thanh "
                    f"{status}!"
                )

                found = True
                break

        if not found:
            print("Khong tim thay mon!")

    elif choice == "4":
        print(
            "\n--- DIEU CHINH GIA GOC CUA MON ---"
        )

        item_id = input(
            "Nhap ma mon can doi gia: "
        )

        found = False

        for item in menu_db:
            if item.item_id == item_id:
                try:
                    new_price = float(
                        input(
                            "Nhap gia tien moi: "
                        )
                    )

                    old_price = item.base_price

                    item.base_price = new_price

                    if (
                        item.base_price
                        != old_price
                    ):
                        print(
                            "Cap nhat gia goc thanh cong!"
                        )

                except ValueError:
                    print(
                        "Gia khong hop le!"
                    )

                found = True
                break

        if not found:
            print("Khong tim thay mon!")

    elif choice == "5":
        print(
            "\n--- CAP NHAT PHU PHI DICH VU TOAN HE THONG ---"
        )

        print(
            f"Phu phi hien tai: "
            f"{MenuItem.service_charge * 100:.0f}%"
        )

        try:
            new_rate = float(
                input(
                    "Nhap phu phi moi. "
                    "Vi du 0.1 tuong ung 10%: "
                )
            )

            MenuItem.update_service_charge(
                new_rate
            )

            print(
                "Cap nhat phu phi dich vu thanh cong!"
            )

        except ValueError:
            print("Du lieu khong hop le!")

    elif choice == "6":
        print(
            "Cam on ban da su dung he thong Rikkei Coffee!"
        )
        break

    else:
        print("Lua chon khong hop le!")
