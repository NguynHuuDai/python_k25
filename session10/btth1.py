cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000],
]

choice = ""

while choice != "5":
    print("\n" + "=" * 60)
    print("        SHOPEE CART MANAGEMENT SYSTEM")
    print("=" * 60)
    print("[1] Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("[2] Thêm sản phẩm mới / Cộng dồn số lượng")
    print("[3] Cập nhật số lượng của một sản phẩm")
    print("[4] Xóa sản phẩm khỏi giỏ hàng")
    print("[5] Thoát chương trình")

    choice = input("\nMời bạn chọn chức năng (1-5): ").strip()

    if choice == "1":
        if len(cart_items) == 0:
            print("\nGiỏ hàng đang trống!")
        else:
            total_quantity = 0
            total_price = 0

            print("\n--- CHI TIẾT GIỎ HÀNG ---")
            print(
                f"{'STT':<5}{'Mã SP':<10}{'Tên Sản Phẩm':<25}{'SL':<5}{'Đơn Giá':<15}{'Thành Tiền':<15}"
            )
            print("-" * 75)

            for i in range(len(cart_items)):
                item = cart_items[i]
                subtotal = item[2] * item[3]

                print(
                    f"{i+1:<5}{item[0]:<10}{item[1]:<25}{item[2]:<5}{item[3]:<15,}{subtotal:<15,}"
                )

                total_quantity += item[2]
                total_price += subtotal

            print("-" * 75)
            print(f"Tổng số lượng sản phẩm: {total_quantity}")
            print(f"Tổng tiền thanh toán  : {total_price:,} đ")

    elif choice == "2":
        product_id = input("Nhập mã sản phẩm: ").strip().upper()
        product_name = input("Nhập tên sản phẩm: ").strip()

        raw_quantity = input("Nhập số lượng: ").strip()
        raw_price = input("Nhập đơn giá: ").strip()

        if not raw_quantity.isdigit() or not raw_price.isdigit():
            print(
                "Lỗi: Số lượng hoặc đơn giá phải là số nguyên dương và không chứa kí tự lạ!"
            )
        else:
            quantity = int(raw_quantity)
            price = int(raw_price)

            if quantity <= 0 or price < 0:
                print("Lỗi: Số lượng phải lớn hơn 0 và đơn giá không được âm!")
            else:
                found = False
                for item in cart_items:
                    if item[0] == product_id:
                        item[2] += quantity
                        found = True
                        print(
                            f"Mã sản phẩm {product_id} đã tồn tại. Hệ thống đã cộng dồn số lượng thành công!"
                        )
                        break

                if not found:
                    cart_items.append(
                        [product_id, product_name, quantity, price])
                    print("Thêm sản phẩm mới vào giỏ hàng thành công!")

    elif choice == "3":
        product_id = input("Nhập mã sản phẩm cần sửa: ").strip().upper()
        raw_new_quantity = input("Nhập số lượng mới: ").strip()

        if not raw_new_quantity.isdigit():
            print("Lỗi: Số lượng mới phải là ký tự số nguyên hợp lệ!")
        else:
            new_quantity = int(raw_new_quantity)

            if new_quantity <= 0:
                print("Lỗi: Số lượng cập nhật phải lớn hơn 0!")
            else:
                found = False
                for item in cart_items:
                    if item[0] == product_id:
                        item[2] = new_quantity
                        found = True
                        print(
                            f"Cập nhật số lượng mới cho sản phẩm {product_id} thành công!"
                        )
                        break

                if not found:
                    print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "4":
        product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()
        found = False

        for item in cart_items:
            if item[0] == product_id:
                cart_items.remove(item)
                found = True
                print(f"Đã xóa hoàn toàn sản phẩm {product_id} khỏi giỏ hàng.")
                break

        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "5":
        print("Đã thoát chương trình quản lý giỏ hàng Shopee. Hẹn gặp lại!")

    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập đúng số từ 1 đến 5.")
