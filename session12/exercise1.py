cart_items = [
    {"id": "P001", "name": "Dien thoai iPhone 15", "number": 1, "price": 25000000},
    {"id": "P002", "name": "Op lung Silicon", "number": 2, "price": 150000},
]

while True:
    print(
        """
======================================================
            SHOPEE CART MANAGEMENT SYSTEM
======================================================
1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm Sản phẩm mới / Cộng dồn số lượng
3. Cập nhật số lượng của một sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
======================================================
"""
    )

    choice = input("Mời bạn chọn chức năng: ").strip()

    if choice == "1":
        if len(cart_items) == 0:
            print("\nGiỏ hàng đang trống!")
        else:
            total_amount = 0
            quantity = 0

            print("\n--- CHI TIẾT GIỎ HÀNG ---")
            print(
                f"{'Mã SP':<10}{'Tên Sản Phẩm':<25}{'SL':<5}{'Đơn Giá':<15}{'Thành Tiền':<15}"
            )
            print("-" * 70)

            for item in cart_items:
                thanh_tien = item["number"] * item["price"]
                total_amount += thanh_tien
                quantity += item["number"]

                print(
                    f"{item['id']:<10}{item['name']:<25}{item['number']:<5}{item['price']:<15,}{thanh_tien:<15,}"
                )

            print("-" * 70)
            print("Tổng số lượng sản phẩm trong giỏ:", quantity)
            print(f"Tổng số tiền thanh toán: {total_amount:,} đ")

    elif choice == "2":
        input_id = input("Nhập mã sản phẩm: ").strip().upper()
        found = False

        for item in cart_items:
            if item["id"] == input_id:
                print("Sản phẩm đã tồn tại, tiến hành cộng dồn số lượng.")
                raw_add_qty = input("Nhập số lượng thêm: ").strip()

                if not raw_add_qty.isdigit():
                    print("Lỗi: Số lượng thêm phải là ký tự số nguyên hợp lệ!")
                else:
                    add_qty = int(raw_add_qty)
                    if add_qty <= 0:
                        print("Lỗi: Số lượng thêm phải lớn hơn 0!")
                    else:
                        item["number"] += add_qty
                        print("Đã cộng dồn số lượng sản phẩm thành công.")
                found = True
                break

        if not found:
            input_name = input("Nhập tên sản phẩm: ").strip()
            raw_price = input("Nhập giá tiền: ").strip()
            raw_number = input("Nhập số lượng: ").strip()

            if not raw_price.isdigit() or not raw_number.isdigit():
                print(
                    "Lỗi: Đơn giá hoặc số lượng phải là ký tự số nguyên hợp lệ!"
                )
            else:
                input_price = int(raw_price)
                input_number = int(raw_number)

                if input_price < 0 or input_number <= 0:
                    print(
                        "Lỗi: Đơn giá không được âm và số lượng phải lớn hơn 0!"
                    )
                else:
                    cart_items.append(
                        {
                            "id": input_id,
                            "name": input_name,
                            "price": input_price,
                            "number": input_number,
                        }
                    )
                    print("Thêm sản phẩm mới vào giỏ hàng thành công!")

    elif choice == "3":
        input_id = input(
            "Nhập vào mã sản phẩm cần cập nhật số lượng: ").strip().upper()
        found = False

        for item in cart_items:
            if item["id"] == input_id:
                raw_number = input("Nhập vào số lượng mới: ").strip()

                if not raw_number.isdigit():
                    print("Lỗi: Số lượng mới phải là ký tự số nguyên hợp lệ!")
                else:
                    input_number = int(raw_number)
                    if input_number <= 0:
                        print("Lỗi: Số lượng cập nhật phải lớn hơn 0!")
                    else:
                        item["number"] = input_number
                        print(
                            f"Cập nhật số lượng mới cho sản phẩm {input_id} thành công!"
                        )
                found = True
                break

        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "4":
        input_id = input("Nhập vào mã sản phẩm cần xóa: ").strip().upper()
        found = False

        for item in cart_items:
            if item["id"] == input_id:
                cart_items.remove(item)
                found = True
                print(f"Đã xóa sản phẩm {input_id} thành công.")
                break

        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "5":
        print("Thoát chương trình...")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại đúng số từ 1 đến 5.")
