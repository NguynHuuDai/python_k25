employee_list = [
    {
        "id": "101",
        "name": "Nguyen Van A",
        "salary": 10.0
    },
    {
        "id": "102",
        "name": "Le Thi B",
        "salary": 15.5
    }
]

while True:
    print("""
======================================
    QUẢN LÝ NHÂN SỰ - STAFF MANAGER
======================================
1. Thêm nhân viên mới
2. Danh sách nhân viên
3. Xóa nhân viên khỏi hệ thống
4. Thoát chương trình
""")

    choice = input("Nhập vào lựa chọn của bạn: ")

    if choice == "1":
        name = input("Nhập vào tên nhân viên mới: ").strip()

        if name == "":
            print("Tên nhân viên không được để trống!")
            continue

        salary = float(input("Nhập vào lương nhân viên: "))
        while salary <= 0:
            print("Mức lương không hợp lệ! ")
            salary = float(input("Nhập vào lương nhân viên: "))

        last_id = int(employee_list[-1]["id"]) # lấy id phần tử cuối và ép về số
        new_id = str(last_id + 1) # tình id kế tiếp và ép lại về chuỗi

        employee_list.append({
            "id": new_id,
            "name": name,
            "salary": salary
        })
        
        print("Đã thêm nhân viên thành công!")

    elif choice == "2":
        if not employee_list:
            print("Chưa có dữ liệu nhân sự!")
            continue

        print("ID    | TÊN NHÂN VIÊN         | MỨC LƯƠNG")
        for emp in employee_list:
            print(f"{emp['id']}   | {emp['name']}      | {emp['salary']}")

    elif choice == "3":
        delete_id = input("Nhập vào id nhân viên muốn xóa: ")
        found = False # kiểm tra có tìm thấy id hay không

        for emp in employee_list:
            if emp["id"] == delete_id:
                employee_list.remove(emp)
                found = True
                print("Đã xóa nhân viên thành công!")
                break

        if not found:
            print("Mã nhân viên không tồn tại!")

    elif choice == "4":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ!")
