order_list = ["GE001", "GE002", "GE003"]
choice = ""
while choice != "4":
    print(f""" 
    ===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
    1. Hiển thị danh sách đơn hàng
    2. Thêm đơn hàng mới
    3. Xóa đơn hàng theo mã
    4. Thoát chương trình
""")
    choice = input("Nhập vào lựa chọn của bạn :")
    if choice == "1":
        print(order_list)
        continue
    elif choice == "2":
        new_input = input("Nhập mã đơn hàng mới :").strip().upper()
        order_list.append(new_input)
        continue
    elif choice == "3":
        delete_input = input("Nhập vào mã đơn hàng muốn xóa :").strip().upper()
        if delete_input in order_list:
            order_list.remove(delete_input)
            print(f"Đã xóa mã {delete_input} khỏi đơn hàng")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa")
    elif choice == "4":
        print("Thoát chương trình")
        break
    