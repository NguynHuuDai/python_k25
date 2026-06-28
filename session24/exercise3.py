class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()
        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    def earn_points(self, bill_amount):
        earned = bill_amount // 10000
        self.__points += earned
        if self.__points >= 100:
            if self.__tier != "VIP":
                print("Chúc mừng! Khách hàng đã được nâng hạng lên VIP.")
            self.__tier = "VIP"
        return earned

    def redeem_points(self, points_to_use):
        if points_to_use <= 0 or points_to_use > self.__points:
            print("Không thể đổi điểm!")
            print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
            print(f"Điểm hiện tại của khách: {self.__points}")
            print("Điểm cũ được giữ nguyên:")
            print(f"Số điểm sau giao dịch: {self.__points}")
            return

        self.__points -= points_to_use
        discount = points_to_use * MemberCard.point_value_vnd
        print(f"Đã trừ {points_to_use} điểm.")
        print(f"Khách hàng được giảm giá {discount:,.0f} VNĐ vào hóa đơn!")
        print(f"Số điểm còn lại: {self.__points}")
        print(f"Hạng thẻ hiện tại: {self.__tier}")

    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value

    @staticmethod
    def is_valid_card_id(card_id):
        if len(card_id) != 4:
            return False
        if card_id[:2] != "RC":
            return False
        return card_id[2:].isdigit()


cards_database = [
    MemberCard("RC01", "Nguyen Van A"),
    MemberCard("RC02", "Tran Thi B")
]

cards_database[0].earn_points(1500000)
cards_database[1].earn_points(200000)


while True:
    print("""
===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====
1. Xem danh sách thẻ thành viên
2. Đăng ký thẻ mới
3. Khách mua hàng (Tích điểm)
4. Khách dùng điểm (Đổi ưu đãi)
5. Cập nhật tỷ giá quy đổi điểm
6. Thoát chương trình
================================================
""")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        if len(cards_database) == 0:
            print("Chưa có thẻ thành viên.")
        else:
            for i, card in enumerate(cards_database, start=1):
                print(
                    f"{i}. Mã: {card.card_id} | "
                    f"Tên: {card.name} | "
                    f"Điểm: {card.points} | "
                    f"Hạng: {card.tier}"
                )

    elif choice == "2":
        print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
        card_id = input("Nhập mã thẻ: ")

        if not MemberCard.is_valid_card_id(card_id):
            print("Mã thẻ không hợp lệ!")
            continue

        duplicate = False
        for card in cards_database:
            if card.card_id == card_id:
                duplicate = True
                break

        if duplicate:
            print("Mã thẻ đã tồn tại trong hệ thống!")
            print("Vui lòng kiểm tra lại.")
            continue

        name = input("Nhập tên khách hàng: ")

        new_card = MemberCard(card_id, name)
        cards_database.append(new_card)

        print("\nĐăng ký thẻ thành viên thành công!")
        print(f"Mã thẻ: {new_card.card_id}")
        print(f"Tên khách hàng: {new_card.name}")
        print(f"Điểm ban đầu: {new_card.points}")
        print(f"Hạng thẻ: {new_card.tier}")

    elif choice == "3":
        print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
        card_id = input("Nhập mã thẻ: ")

        found = None
        for card in cards_database:
            if card.card_id == card_id:
                found = card
                break

        if found is None:
            print("Không tìm thấy thẻ.")
            continue

        bill = int(input("Nhập tổng tiền hóa đơn: "))

        earned = found.earn_points(bill)

        print(f"\nKhách hàng: {found.name}")
        print(f"Hóa đơn: {bill:,.0f} VNĐ")
        print(f"Số điểm được tích: {earned}")
        print(f"Tổng điểm hiện tại: {found.points}")
        print(f"Hạng thẻ hiện tại: {found.tier}")
    elif choice == "4":
        print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
        card_id = input("Nhập mã thẻ: ")

        found = None
        for card in cards_database:
            if card.card_id == card_id:
                found = card
                break

        if found is None:
            print("Không tìm thấy thẻ.")
            continue

        points = int(input("Nhập số điểm muốn sử dụng: "))
        found.redeem_points(points)

    elif choice == "5":
        print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
        print(
            f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,.0f} VNĐ")

        new_value = int(input("Nhập tỷ giá mới cho 1 điểm: "))

        if new_value <= 0:
            print("Tỷ giá không hợp lệ!")
            continue

        MemberCard.update_point_value(new_value)

        print("\nCập nhật tỷ giá thành công!")
        print(f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,.0f} VNĐ")

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
