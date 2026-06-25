class BistroTable:
    _vat_rate = 0.08

    def __init__(self, table_id, capacity):
        self.__table_id = table_id
        self.capacity = capacity
        self.__current_bill = 0

    @property
    def table_id(self):
        return self.__table_id

    @property
    def current_bill(self):
        return self.__current_bill

    @property
    def status(self):
        if self.__current_bill == 0:
            return "Dang trong"
        return "Co khach"

    @property
    def total_payment(self):
        return self.__current_bill * (1 + BistroTable._vat_rate)

    def order_dish(self, amount):
        self.__current_bill += amount

    def cancel_dish(self, amount):
        if amount > self.__current_bill:
            print("Loi: So tien giam tru vuot qua gia tri hoa don hien tai!")
            return False

        self.__current_bill -= amount
        return True

    def checkout(self):
        total = self.total_payment
        self.__current_bill = 0
        return total

    @classmethod
    def update_vat_rate(cls, new_rate):
        cls._vat_rate = new_rate

    @staticmethod
    def is_valid_table_id(table_id):
        if table_id.startswith("TB") and len(table_id) >= 3:
            return True
        return False


table_records = [
    BistroTable("TB01", 4),
    BistroTable("TB02", 2),
    BistroTable("TB03", 8)
]


def find_table(table_id):
    for table in table_records:
        if table.table_id == table_id:
            return table
    return None


def main():
    while True:
        print("\n===== HE THONG DIEU PHOI BAN AN - RIKKEI BISTRO =====")
        print("1. Hien thi so do & Trang thai ban an")
        print("2. Goi mon moi (Tang tien hoa don)")
        print("3. Huy mon / Giam tru hoa don")
        print("4. Cap nhat thue suat VAT toan nha hang")
        print("5. Thanh toan hoa don & Tra ban trong")
        print("6. Thoat chuong trinh")
        print("=====================================================")

        choice = input("Chon chuc nang (1-6): ")

        if choice == "1":
            print("\n--- SO DO BAN AN RIKKEI BISTRO ---")

            for index, table in enumerate(table_records, start=1):
                print(
                    f"{index}. Ma ban: {table.table_id} | "
                    f"Suc chua: {table.capacity} nguoi | "
                    f"Tam tinh: {table.current_bill:,.0f}d | "
                    f"Trang thai: {table.status}"
                )

            print("----------------------------------")

        elif choice == "2":
            print("\n--- GOI MON MOI ---")

            table_id = input("Nhap ma ban goi mon: ").upper()

            if not BistroTable.is_valid_table_id(table_id):
                print("Ma ban khong hop le!")
                continue

            table = find_table(table_id)

            if table is None:
                print("Khong tim thay ban!")
                continue

            try:
                amount = int(input("Nhap gia tien mon an moi: "))

                if amount <= 0:
                    print("Vui long nhap so tien la mot so nguyen duong!")
                    continue

                table.order_dish(amount)

                print(
                    f">> Thanh cong: Da ghi nhan mon an "
                    f"{amount:,.0f}d vao Ban '{table.table_id}'."
                )

                print(
                    f">> So tien tam tinh hien tai cua ban: "
                    f"{table.current_bill:,.0f}d."
                )

            except ValueError:
                print("Vui long nhap so tien la mot so nguyen duong!")

        elif choice == "3":
            print("\n--- HUY MON / GIAM TRU HOA DON ---")

            table_id = input("Nhap ma ban can huy mon: ").upper()

            if not BistroTable.is_valid_table_id(table_id):
                print("Ma ban khong hop le!")
                continue

            table = find_table(table_id)

            if table is None:
                print("Khong tim thay ban!")
                continue

            try:
                amount = int(
                    input("Nhap gia tri mon muon giam tru: ")
                )

                if amount <= 0:
                    print("Vui long nhap so tien la mot so nguyen duong!")
                    continue

                result = table.cancel_dish(amount)

                if result:
                    print(
                        f">> Thanh cong: Da giam tru "
                        f"{amount:,.0f}d khoi Ban "
                        f"'{table.table_id}' do su co bep."
                    )

                    print(
                        f">> So tien tam tinh con lai: "
                        f"{table.current_bill:,.0f}d."
                    )

                    if table.current_bill == 0:
                        print(
                            f">> Ban '{table.table_id}' hien da "
                            f"chuyen ve trang thai Dang trong."
                        )

            except ValueError:
                print("Vui long nhap so tien la mot so nguyen duong!")

        elif choice == "4":
            print(
                "\n--- CAP NHAT THUE SUAT VAT TOAN NHA HANG ---"
            )

            print(
                f"[HE THONG] Thue suat VAT hien tai la: "
                f"{BistroTable._vat_rate * 100:.0f}% "
                f"({BistroTable._vat_rate})"
            )

            try:
                new_rate = float(
                    input(
                        "Nhap thue suat VAT moi "
                        "(vi du: 0.1 cho 10%): "
                    )
                )

                if new_rate < 0 or new_rate > 0.2:
                    print("Ty le thue khong hop le!")
                    continue

                BistroTable.update_vat_rate(new_rate)

                print(
                    f"\n>> Thong bao: Rikkei Bistro "
                    f"cap nhat thue suat VAT moi o muc "
                    f"{new_rate * 100:.0f}% thanh cong!"
                )

            except ValueError:
                print("Ty le thue khong hop le!")

        elif choice == "5":
            print("\n--- THANH TOAN HOA DON ---")

            table_id = input(
                "Nhap ma ban thanh toan: "
            ).upper()

            if not BistroTable.is_valid_table_id(table_id):
                print("Ma ban khong hop le!")
                continue

            table = find_table(table_id)

            if table is None:
                print("Khong tim thay ban!")
                continue

            if table.current_bill == 0:
                print(
                    "Loi: Ban nay hien dang trong, "
                    "khong co hoa don de thanh toan!"
                )
                continue

            bill = table.current_bill
            total = table.total_payment

            print(
                f"\n--- HOA DON THANH TOAN BAN "
                f"{table.table_id} ---"
            )

            print(f"So tien mon an: {bill:,.0f}d")

            print(
                f"Thue suat VAT ap dung: "
                f"{BistroTable._vat_rate * 100:.0f}%"
            )

            print(
                f"Tong tien can thanh toan "
                f"(gom thue): {total:,.0f}d"
            )

            print("-----------------------------------")

            table.checkout()

            print(
                f">> Thanh toan thanh cong! "
                f"Ban '{table.table_id}' da duoc "
                f"don sach va chuyen sang trang thai Dang trong."
            )

        elif choice == "6":
            print(
                "Cam on ban da su dung he thong "
                "dieu phoi ban an Rikkei Bistro!"
            )
            break

        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()
