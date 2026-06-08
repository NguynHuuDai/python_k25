
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:

    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

   
    if choice == "1":

        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("\nDanh sách sản phẩm hiện tại:")

            for i in range(len(product_list)):

                if product_list[i]["quantity"] == 0:
                    status = "Hết hàng"
                elif product_list[i]["quantity"] <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"

                print(
                    f"{i + 1}. Mã SP: {product_list[i]['product_id']} | "
                    f"Tên: {product_list[i]['product_name']} | "
                    f"Giá: {product_list[i]['price']} | "
                    f"Tồn kho: {product_list[i]['quantity']} | "
                    f"Đã bán: {product_list[i]['sold']} | "
                    f"Trạng thái: {status}"
                )

    elif choice == "2":

        product_id = input(
            "Nhập mã sản phẩm khách muốn mua: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                quantity_buy = input(
                    "Nhập số lượng khách mua: "
                )

                if not quantity_buy.isdigit() or int(quantity_buy) <= 0:
                    print("Số lượng mua không hợp lệ")
                    break

                quantity_buy = int(quantity_buy)

                if quantity_buy > product["quantity"]:
                    print("Số lượng trong kho không đủ để bán")
                    break

                product["quantity"] -= quantity_buy
                product["sold"] += quantity_buy

                total_price = quantity_buy * product["price"]

                print("Bán sản phẩm thành công")
                print("Khách cần thanh toán:", total_price)

                break

        if not found:
            print("Không tìm thấy sản phẩm cần bán")

    
    elif choice == "3":

        product_id = input(
            "Nhập mã sản phẩm cần nhập thêm: "
        ).strip().upper()

        found = False

        for product in product_list:

            if product["product_id"] == product_id:

                found = True

                quantity_import = input(
                    "Nhập số lượng nhập thêm: "
                )

                if not quantity_import.isdigit() or int(quantity_import) <= 0:
                    print("Số lượng nhập kho không hợp lệ")
                    break

                product["quantity"] += int(quantity_import)

                print("Nhập kho thành công")

                break

        if not found:
            print("Không tìm thấy sản phẩm cần nhập kho")

    elif choice == "4":

        total_revenue = 0
        best_seller = ""
        max_sold = 0

        sold_check = False

        for product in product_list:
            if product["sold"] > 0:
                sold_check = True
                break

        if not sold_check:
            print("Chưa có doanh thu phát sinh")

        else:

            print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")

            for i in range(len(product_list)):

                revenue = (
                    product_list[i]["price"]
                    * product_list[i]["sold"]
                )

                total_revenue += revenue

                print(
                    f"{i + 1}. "
                    f"{product_list[i]['product_name']} | "
                    f"Đã bán: {product_list[i]['sold']} | "
                    f"Doanh thu: {revenue}"
                )

                if product_list[i]["sold"] > max_sold:
                    max_sold = product_list[i]["sold"]
                    best_seller = product_list[i]["product_name"]

            print("\nTổng doanh thu:", total_revenue)
            print("Sản phẩm bán chạy nhất:", best_seller)

    elif choice == "5":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
