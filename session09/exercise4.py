order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

choice = ""

while choice != "4":
    print("""
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Cập nhật danh sách đơn hàng
3. Thống kê đơn hàng theo trạng thái
4. Thoát chương trình
""")

    choice = input("Nhập vào lựa chọn của bạn: ")

    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i in range(len(order_list)):
                print(f"{i + 1}. {order_list[i]}")

    elif choice == "2":
        new_choice = ""

        while new_choice != "4":
            print("""
----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----
1. Thêm đơn hàng mới
2. Sửa đơn hàng theo vị trí
3. Xóa đơn hàng theo vị trí
4. Quay lại menu chính
""")

            new_choice = input("Nhập vào lựa chọn của bạn: ")

            if new_choice == "1":
                new_code = input("Nhập mã đơn hàng: ").strip().upper()
                new_status = input(
                    "Nhập trạng thái đơn hàng: ").strip().upper()

                order_list.append(new_code + " - " + new_status)

                print("Thêm đơn hàng thành công!")

            elif new_choice == "2":
                index_update = input("Nhập vị trí cần sửa: ")

                if index_update.isdigit():
                    index_update = int(index_update)

                    if 1 <= index_update <= len(order_list):
                        new_code = input(
                            "Nhập mã đơn hàng mới: ").strip().upper()
                        new_status = input(
                            "Nhập trạng thái mới: ").strip().upper()

                        order_list[index_update - 1] = new_code + \
                            " - " + new_status

                        print("Cập nhật đơn hàng thành công!")
                    else:
                        print("Không tồn tại đơn hàng ở vị trí này!")
                else:
                    print("Vị trí không hợp lệ!")

            elif new_choice == "3":
                index_delete = input("Nhập vị trí cần xóa: ")

                if index_delete.isdigit():
                    index_delete = int(index_delete)

                    if 1 <= index_delete <= len(order_list):
                        deleted_order = order_list[index_delete - 1]
                        del order_list[index_delete - 1]

                        print("Đã xóa đơn hàng:", deleted_order)
                    else:
                        print("Không tồn tại đơn hàng ở vị trí này!")
                else:
                    print("Vị trí không hợp lệ!")

            elif new_choice == "4":
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

    elif choice == "3":
        pending = 0
        delivering = 0
        completed = 0
        cancelled = 0

        for order in order_list:
            status = order.split(" - ")[1]

            if status == "PENDING":
                pending += 1
            elif status == "DELIVERING":
                delivering += 1
            elif status == "COMPLETED":
                completed += 1
            elif status == "CANCELLED":
                cancelled += 1

        print("""
===== THỐNG KÊ ĐƠN HÀNG =====
""")
        print("PENDING:", pending)
        print("DELIVERING:", delivering)
        print("COMPLETED:", completed)
        print("CANCELLED:", cancelled)
        print("Tổng số đơn hàng:", len(order_list))

    elif choice == "4":
        print("Thoát chương trình")

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
