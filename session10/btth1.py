cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
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

    choice = input("\nMời bạn chọn chức năng (1-5): ")

    if choice == "1":

        if len(cart_items) == 0:
            print("\nGiỏ hàng đang trống!")
        else:

            total_quantity = 0
            total_money = 0

            print("\n--- CHI TIẾT GIỎ HÀNG ---")
            print(
                f"{'STT':<5}{'Mã SP':<10}{'Tên Sản Phẩm':<25}{'SL':<5}{'Đơn Giá':<15}{'Thành Tiền':<15}"
            )

            for i in range(len(cart_items)):
                item = cart_items[i]

                thanh_tien = item[2] * item[3]

                print(
                    f"{i+1:<5}{item[0]:<10}{item[1]:<25}{item[2]:<5}{item[3]:<15,}{thanh_tien:<15,}"
                )

                total_quantity += item[2]
                total_money += thanh_tien

            print("-" * 80)
            print("Tổng số lượng sản phẩm:", total_quantity)
            print("Tổng tiền thanh toán:", format(total_money, ","), "đ")

    elif choice == "2":

        product_id = input("Nhập mã sản phẩm: ")
        product_name = input("Nhập tên sản phẩm: ")

        quantity = int(input("Nhập số lượng: "))
        price = int(input("Nhập đơn giá: "))

        if quantity <= 0 or price < 0:
            print("Lỗi: Số lượng hoặc đơn giá không hợp lệ!")

        else:

            found = False

            for item in cart_items:

                if item[0] == product_id:
                    item[2] += quantity
                    found = True
                    print("Đã cộng dồn số lượng sản phẩm.")
                    break

            if not found:
                cart_items.append(
                    [product_id, product_name, quantity, price]
                )
                print("Thêm sản phẩm thành công!")

    elif choice == "3":

        product_id = input("Nhập mã sản phẩm: ")
        new_quantity = int(input("Nhập số lượng mới: "))

        if new_quantity <= 0:
            print("Lỗi: Số lượng phải lớn hơn 0!")

        else:

            found = False

            for item in cart_items:

                if item[0] == product_id:

                    item[2] = new_quantity

                    found = True

                    print("Cập nhật số lượng thành công!")

                    break

            if not found:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "4":

        product_id = input("Nhập mã sản phẩm cần xóa: ")

        found = False

        for item in cart_items:

            if item[0] == product_id:

                cart_items.remove(item)

                found = True

                print("Xóa sản phẩm thành công!")

                break

        if not found:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "5":

        print("Đã thoát!")

    else:

        print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")
