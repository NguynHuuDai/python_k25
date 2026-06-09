cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]

while True:
    print("""
======================================================
            SHOPEE CART MANAGEMENT SYSTEM
======================================================
1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm Sản phẩm mới / Cộng dồn số lượng
3. Cập nhật số lượng của một sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
======================================================
""")

    choice = input("Mời bạn chọn chức năng: ")

    if choice == "1":
        total_amount = 0
        quantity = 0

        for item in cart_items:
            thanh_tien = item["number"] * item["price"]
            total_amount += thanh_tien
            quantity += item["number"]

            print(
                f"{item['id']} | {item['name']} | {item['number']} | {item['price']} | {thanh_tien}")

        print("Tổng số lượng sản phẩm trong giỏ:", quantity)
        print("Tổng số tiền thanh toán:", total_amount)

    elif choice == "2":
        input_id = input("Nhập mã sản phẩm: ")

        found = False

        for item in cart_items:
            if item["id"] == input_id:
                print("Sản phẩm đã tồn tại, cộng dồn số lượng")
                add_qty = int(input("Nhập số lượng thêm: "))
                item["number"] += add_qty
                found = True
                break

        if not found:
            input_name = input("Nhập tên sản phẩm: ")
            input_price = int(input("Nhập giá tiền: "))
            input_number = int(input("Nhập số lượng: "))

            if input_price <= 0 or input_number <= 0:
                print("Giá hoặc số lượng không hợp lệ")
            else:
                cart_items.append({
                    "id": input_id,
                    "name": input_name,
                    "price": input_price,
                    "number": input_number
                })
    elif choice == "3":
        input_id = input("Nhập vào mã sản phẩm cần cập nhập số lượng: ").upper()
        found = False
        for item in cart_items:
            if item["id"] == input_id:
                input_number = int(input("Nhập vào số lượng mới: "))
                item["number"] = input_number
                found = True
                break

        if not found:
            print("Mã sản phẩm không tồn tại.")
            break
    
    elif choice == "4":
        input_id = input("Nhập vào mã sản phẩm cần xóa: ").upper()
        found = False

        for index, item in enumerate(cart_items):
            if item["id"] == input_id:
                del cart_items[index]
                found = True          
                print(f"Đã xóa sản phẩm {input_id} thành công.")
                break

        if not found:
            print("Mã sản phẩm không tồn tại.")

    elif choice == "5":
        print("Thoát chương trình...")
        break
