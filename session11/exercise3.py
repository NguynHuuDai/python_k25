product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":

        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")

            for i in range(len(product_list)):
                print(
                    f"{i + 1}. Mã SP: {product_list[i]['product_id']} | "
                    f"Tên: {product_list[i]['product_name']} | "
                    f"Giá: {product_list[i]['price']} | "
                    f"Số lượng: {product_list[i]['quantity']}"
                )

    elif choice == "2":

        product_id = input("Nhập mã sản phẩm: ").strip().upper()

        check_duplicate = False

        for product in product_list:
            if product["product_id"] == product_id:
                check_duplicate = True
                break

        if check_duplicate:
            print("Mã sản phẩm bị trùng")
            continue

        product_name = input("Nhập tên sản phẩm: ")

        price = input("Nhập giá sản phẩm: ")

        if not price.isdigit() or int(price) <= 0:
            print("Giá không hợp lệ")
            continue

        quantity = input("Nhập số lượng sản phẩm: ")

        if not quantity.isdigit() or int(quantity) <= 0:
            print("Số lượng không hợp lệ")
            continue

        new_product = {
            "product_id": product_id,
            "product_name": product_name,
            "price": int(price),
            "quantity": int(quantity)
        }

        product_list.append(new_product)

        print("Thêm sản phẩm thành công")

    elif choice == "3":

        product_id = input(
            "Nhập mã sản phẩm cần cập nhật: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                product_name = input("Nhập tên mới: ")

                price = input("Nhập giá mới: ")

                if not price.isdigit() or int(price) <= 0:
                    print("Giá không hợp lệ")
                    break

                quantity = input("Nhập số lượng mới: ")

                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Số lượng không hợp lệ")
                    break

                product["product_name"] = product_name
                product["price"] = int(price)
                product["quantity"] = int(quantity)

                print("Cập nhật sản phẩm thành công")
                break

        if not found:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")

    elif choice == "4":

        product_id = input(
            "Nhập mã sản phẩm cần xoá: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                product_list.remove(product)

                found = True

                print("Xóa sản phẩm thành công")
                break

        if not found:
            print("Không tìm thấy mã sản phẩm cần xoá!")

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")